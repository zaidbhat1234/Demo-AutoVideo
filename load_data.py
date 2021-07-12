from autovideo.utils import set_log_path, logger

set_log_path(log_path) #Setup logger

train_table_path = os.path.join(args.data_dir, 'train.csv')
train_media_dir = os.path.join(args.data_dir, 'media')
target_index = 2

# Read the CSV file
train_dataset = pd.read_csv(train_table_path)
