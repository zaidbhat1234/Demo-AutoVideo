import ray
from ray import tune
from hyperopt import hp

#Search Space
search_space = {
    "algorithm": tune.choice(["tsn"]),
    "learning_rate": tune.uniform(0.0001, 0.001),
    "momentum": tune.uniform(0.9,0.99),
    "weight_decay": tune.uniform(5e-4,1e-3),
    "num_segments": tune.choice([8,16,32]),
}

# Tuning
config = {
    "searching_algorithm": args.alg,
    "num_samples": args.num_samples,
}
