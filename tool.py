import argparse, subprocess

def main(args):
    source_url = args.url
    print("Downloading video from: " + source_url)
    
    print()
    
    download_args = ['--ignore-config', '-N', '4', '--embed-thumbnail', '-o', '%(title)s.%(ext)s']
    if args.cookies:
        download_args.append('--cookies-from-browser')
        download_args.append('firefox')
    
    if args.extract_audio:
        download_args.append('-x')
        download_args.append('--audio-format')
        download_args.append('mp3')
    else:
        # Download best format that contains video,
        # and if it doesn't already have an audio stream, merge it with best audio-only format
        download_args.append('-f')
        download_args.append('bv*+ba/b')
    
    cmd_args = ['yt-dlp'] + download_args + [source_url]
    cp = subprocess.run(cmd_args)

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='URL of the video to download')
    parser.add_argument('-c', '--cookies', action='store_true', help='Use cookies to login')
    parser.add_argument('-x', '--extract-audio', action='store_true', help='Extract audio from video')
    args = parser.parse_args()
    main(args)

if __name__ == '__main__':
    parse()