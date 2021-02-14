"""Python file used for logging data to a CSV file."""
import json


class Logger:
    """The Logger class is responsible for logging data to a CSV file by appending to the end of the file."""

    operation = None
    num_process = None
    num_neighbors = None
    alpha = None
    train_epoch = None
    latent_factors = None
    regularization_factor = None
    hyper_optimization = None
    hyper_epoch = None

    def __init__(self, operation: str) -> None:
        """Constructor for the Logger class.

        Args:
            operation (str): The type of algorithm used.
        """
        # First, load the config file and check if it can be loaded
        config_file = None
        try:
            config_file = json.load(open("config.json", "r"))
        except Exception as e:
            print("Exception raised.")
            print(e.__doc__)
            print("Check if config file exists and is in good order")
        # Save the parameters from the config file
        self.operation = operation
        self.num_process = config_file["number_processes"]
        self.num_neighbors = config_file["number_neighbours"]
        self.alpha = config_file["alpha"]
        self.train_epoch = config_file["train_epoch"]
        self.latent_factors = config_file["latent_factors"]
        self.regularization_factor = config_file["regularization_factor"]
        self.hyper_optimization = config_file["hyper_optimization"]
        self.hyper_epoch = config_file["hyper_epoch"]

    def save(self, rmse: float, time: float) -> None:
        """Appends the data to the CSV file

        Args:
            rmse (float): The Root Mean Squared Error of the algorithm on the test set.
            time (float): The time taken for the algorithm to complete.
        """
        log = self.operation + ", " + str(rmse) + ", " + str(time) + ", " \
            + str(self.num_process) + ", " \
            + ", " + str(self.num_neighbors) \
            + ", " + str(self.alpha) + ", " + str(self.train_epoch) \
            + ", " + str(self.latent_factors) + ", " \
            + str(self.regularization_factor) + ", " \
            + str(self.hyper_optimization) \
            + ", " + str(self.hyper_epoch) + "\n"
        print("log: " + log)
        try:
            with open('logs.csv', 'a', newline='') as fd:
                fd.write(log)
        except Exception as e:
            print("Exception raised.")
            print(e.__doc__)
            print("Check if config file exists and is in good order")
