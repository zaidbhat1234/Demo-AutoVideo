# Load fitted pipeline
import torch
fitted_pipeline = torch.load(args.load_path)

# Produce
predictions = produce(test_dataset=test_dataset,
                    test_media_dir=test_media_dir,
                    target_index=target_index,
                    fitted_pipeline=fitted_pipeline)

# Get accuracy
test_acc = compute_accuracy_with_preds(predictions['label'], test_labels)
