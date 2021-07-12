# Build pipeline based on configs
# Here we can specify the hyperparameters defined in each primitive
# The default hyperparameters will be used if not specified
config = {
    "algorithm": args.alg,
    "load_pretrained": args.pretrained,
}
pipeline = build_pipeline(config)
