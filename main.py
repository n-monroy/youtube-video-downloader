import os
import sys
import yt_dlp


def get_download_path():
    """Return the download directory, creating it if needed."""
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "downloads")
    os.makedirs(path, exist_ok=True)
    return path


def build_yt_dlp_options(output_dir: str, resolution: str = "1080") -> dict:
    """
    Build yt-dlp options dict.

    - Tries to get the requested resolution (default 1080p) with audio merged.
    - Falls back to best available if the resolution isn't offered.
    - Merges into mp4 automatically (requires ffmpeg on PATH).
    """
    return {
        # Prefer requested resolution mp4 video + best audio, fallback to best overall.
        # The last fallback ("best") picks a pre-merged progressive stream that
        # doesn't require ffmpeg for muxing.
        "format": (
            f"bestvideo[height<={resolution}][ext=mp4]+bestaudio[ext=m4a]/"
            f"bestvideo[height<={resolution}]+bestaudio/"
            "best"
        ),
        "merge_output_format": "mp4",
        "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
        "noplaylist": True,
        "progress_hooks": [_progress_hook],
        "postprocessor_hooks": [_postprocessor_hook],
        # Embed metadata tags (title, artist, etc.) into the mp4 file.
        # Requires ffmpeg to be installed and available on PATH.
        # Install with:  winget install ffmpeg  (then restart your terminal)
        # If ffmpeg is not installed, the download will still work but this
        # postprocessing step will fail with:
        #   "ERROR: Postprocessing: ffmpeg not found"
        "postprocessors": [
            {"key": "FFmpegMetadata"},
        ],
    }


def _progress_hook(d: dict):
    """Pretty progress bar printed to the console."""
    if d["status"] == "downloading":
        total = d.get("total_bytes") or d.get("total_bytes_estimate") or 0
        downloaded = d.get("downloaded_bytes", 0)
        speed = d.get("speed")
        eta = d.get("eta")

        if total > 0:
            pct = downloaded / total * 100
            bar_len = 30
            filled = int(bar_len * downloaded // total)
            bar = "█" * filled + " " * (bar_len - filled)
            parts = [f"\r[{bar}] {pct:5.1f}%"]
        else:
            parts = [f"\r  {downloaded / 1_048_576:.1f} MB"]

        if speed:
            parts.append(f"  {speed / 1_048_576:.1f} MB/s")
        if eta:
            parts.append(f"  ETA {eta}s")

        print("".join(parts), end="", flush=True)

    elif d["status"] == "finished":
        print("\nDownload complete. Merging/processing...")


def _postprocessor_hook(d: dict):
    """Called after post-processing (merging audio+video, etc.)."""
    if d["status"] == "finished":
        print(f"Saved: {d.get('info_dict', {}).get('filepath', '')}")


def print_video_info(info: dict):
    """Print useful metadata about the video."""
    duration_s = info.get("duration")
    if duration_s:
        mins, secs = divmod(int(duration_s), 60)
        hours, mins = divmod(mins, 60)
        dur_str = f"{hours}:{mins:02d}:{secs:02d}" if hours else f"{mins}:{secs:02d}"
    else:
        dur_str = "unknown"

    print(f"\nTitle:      {info.get('title', 'N/A')}")
    print(f"Channel:    {info.get('channel', info.get('uploader', 'N/A'))}")
    print(f"Duration:   {dur_str}")
    print(f"Views:      {info.get('view_count', 'N/A'):,}" if isinstance(info.get("view_count"), int) else "")
    print(f"Resolution: {info.get('resolution', 'N/A')}")
    print()


def download(url: str, resolution: str = "1080"):
    """Download a single YouTube video."""
    output_dir = get_download_path()
    opts = build_yt_dlp_options(output_dir, resolution)

    with yt_dlp.YoutubeDL(opts) as ydl:
        # Extract info first to display metadata before downloading
        info = ydl.extract_info(url, download=False)
        print_video_info(info)

        # Now download
        ydl.download([url])

    print("\nVideo downloaded successfully!")


def main():
    # ── Configure your download here ──────────────────────────────────
    # You can pass a URL as a command-line argument:
    #   python main.py "https://www.youtube.com/watch?v=VIDEO_ID"
    # Or change the default URL below.
    default_url = "https://www.youtube.com/watch?v=iOAvc2HcAwY"
    url = sys.argv[1] if len(sys.argv) > 1 else default_url

    # Max resolution: "1080", "720", "480", "360", or "best"
    resolution = "1080"
    # ──────────────────────────────────────────────────────────────────

    try:
        download(url, resolution)
    except yt_dlp.utils.DownloadError as e:
        print(f"\nDownload failed: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nDownload cancelled.")
        sys.exit(0)


if __name__ == "__main__":
    main()
