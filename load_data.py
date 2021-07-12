from autovideo.utils import set_log_path

set_log_path('log.txt') #Setup logger
data_dir = 'datasets/hmdb6/' #Directory containing dataset (hmdb-6)

train_table_path = os.path.join(data_dir, 'train.csv')
train_media_dir = os.path.join(data_dir, 'media')
target_index = 2 #Index of column containing label information

# Read the CSV file
train_dataset = pd.read_csv(train_table_path)
