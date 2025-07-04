#!/usr/bin/env python3
"""
Cleanup script for temporary files created by the Dream Synthesizer application.
Can be run manually or scheduled as a cron job/task scheduler task.
"""

import os
import sys
import argparse
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

# Add the src directory to the path for imports
script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(script_dir)
src_dir = os.path.join(project_dir, 'src')
sys.path.append(src_dir)

# Make sure we can import both with and without src prefix
sys.path.append(project_dir)

# Import our helper functions
from src.utils.helpers import clean_up_temp_files, clean_temp_images

def parse_args():
    parser = argparse.ArgumentParser(description='Clean up temporary files created by the Dream Synthesizer app')
    parser.add_argument('--max-age', type=int, default=24, help='Maximum age of files to keep (in hours)')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be deleted without deleting')
    parser.add_argument('--path', type=str, default=None, help='Path to clean (defaults to project directory)')
    return parser.parse_args()

def main():
    args = parse_args()
    
    # Use provided path or default to project directory
    target_path = args.path if args.path else project_dir
    
    logging.info(f"Starting cleanup of temporary files in {target_path}")
    logging.info(f"Max file age: {args.max_age} hours")
    logging.info(f"Dry run: {args.dry_run}")
    
    if args.dry_run:
        logging.info("DRY RUN - no files will be deleted")
    
    # Clean temporary audio files
    audio_patterns = ['*.wav.tmp', 'temp_*.wav', 'temp_*.mp3']
    for pattern in audio_patterns:
        if not args.dry_run:
            deleted, freed = clean_up_temp_files(target_path, pattern, args.max_age)
            if deleted > 0:
                logging.info(f"Deleted {deleted} {pattern} files ({freed/1024/1024:.2f} MB)")
        else:
            # In dry run, just count files that would be deleted
            import glob
            from datetime import datetime, timedelta
            cutoff_time = datetime.now() - timedelta(hours=args.max_age)
            files = glob.glob(os.path.join(target_path, pattern))
            would_delete = 0
            would_free = 0
            for file_path in files:
                file_stats = os.stat(file_path)
                last_modified = datetime.fromtimestamp(file_stats.st_mtime)
                if last_modified < cutoff_time:
                    would_delete += 1
                    would_free += file_stats.st_size
            if would_delete > 0:
                logging.info(f"Would delete {would_delete} {pattern} files ({would_free/1024/1024:.2f} MB)")
    
    # Clean temporary image files
    if not args.dry_run:
        deleted, freed = clean_temp_images(target_path, args.max_age)
        if deleted > 0:
            logging.info(f"Deleted {deleted} temporary image files ({freed/1024/1024:.2f} MB)")
    else:
        # Equivalent dry run for image files
        total_would_delete = 0
        total_would_free = 0
        for pattern in ['temp_*.png', 'temp_*.jpg', 'temp_*.jpeg', 'temp_*.gif']:
            import glob
            from datetime import datetime, timedelta
            cutoff_time = datetime.now() - timedelta(hours=args.max_age)
            files = glob.glob(os.path.join(target_path, pattern))
            for file_path in files:
                file_stats = os.stat(file_path)
                last_modified = datetime.fromtimestamp(file_stats.st_mtime)
                if last_modified < cutoff_time:
                    total_would_delete += 1
                    total_would_free += file_stats.st_size
        if total_would_delete > 0:
            logging.info(f"Would delete {total_would_delete} temporary image files ({total_would_free/1024/1024:.2f} MB)")
    
    logging.info("Cleanup completed")

if __name__ == "__main__":
    main()
