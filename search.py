from autovideo.searcher import RaySearcher
searcher = RaySearcher(
        train_dataset=train_dataset,
        train_media_dir=train_media_dir,
        valid_dataset=valid_dataset,
        valid_media_dir=valid_media_dir
)
best_config = searcher.search(
        search_space=search_space,
        config=config
)
