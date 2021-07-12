from autovideo import fit, extract_frames


# Extract frames from the video
video_ext = train_dataset.iloc[0, 1].split('.')[-1]
extract_frames(train_media_dir, video_ext)
