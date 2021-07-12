from autovideo import fit
import torch

# Fit
_, fitted_pipeline = fit(train_dataset=train_dataset,
                        train_media_dir=train_media_dir,
                        target_index=target_index,
                        pipeline=pipeline)

# Save the fitted pipeline
torch.save(fitted_pipeline, 'weights/')
