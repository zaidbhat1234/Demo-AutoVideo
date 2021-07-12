# Build pipeline based on configs
# Here we can specify the hyperparameters defined in each primitive
# The default hyperparameters will be used if not specified
from autovideo import build_pipeline

alg = 'tsn' #Specify the Action Recognition algorithm to use. In this example we use TSN
pretrained = True #To fine tune from pretrained weights
config = {
    "algorithm": alg,
    "load_pretrained": pretrained,
}
pipeline = build_pipeline(config)
