"""Python file used to generate numpy matrices from movie ratings file
"""
import numpy as np
import json
import os


class MatrixMaker:
    """The MatrixMaker class is responsible for generating the matrices but also checking if they already exist
    """
    ratings_file = None
    config_file = None
    train_file_name = None
    test_file_name = None
    validation_file_name = None
    utility_file_name = None

    def __init__(self, ratings_file: str = "") -> None:
        """Constructor for the MatrixMaker class

        Args:
            ratings_file (str, optional): [Overrides the ratings file path from the config file]. Defaults to "".
        """        
        # First, load the config file and check if it can be loaded
        try:
            self.config_file = json.load(open("config.json", "r"))
        except Exception as e:
            print("Exception raised.")
            print(e.__doc__)
            print("Check if config file exists and is in good order")

        # For default, use the ratings file path from the config file
        # Otherwise, you get the provided path.
        if ratings_file == "":
            self.ratings_file = self.config_file["ratings_file_path"]
        else: 
            self.ratings_file = ratings_file

        # Finally, create the file names for the matrices
        folder_path = self.config_file["matrices_folder_path"]
        self.train_file_name = folder_path+self.config_file["train_set_file_name"]+".npy"
        self.test_file_name = folder_path+self.config_file["test_set_file_name"]+".npy"
        self.validation_file_name = folder_path+self.config_file["validation_set_file_name"]+".npy"
        self.utility_file_name = folder_path+self.config_file["utility_matrix_file_name"]+".npy"

    def make_matrices(self, remake: bool = False) -> (np.ndarray, np.ndarray, np.ndarray, np.ndarray):
        """The method used to create matrices from the ratings file and return them

        Args:
            remake (bool, optional): [Force the script to reconstruct the matrices]. Defaults to False.

        Returns:
            (np.ndarray, np.ndarray, np.ndarray, np.ndarray): tuple of the 4 matrices (train, test, validation, utility)
        """     
        if(self.__check_files() and not remake):
            print("Files found, returning the matrices.")
            return (np.load(self.train_file_name), np.load(self.test_file_name), np.load(self.validation_file_name), np.load(self.utility_file_name))
        print("Files not found, generating files.")
        ratings = np.genfromtxt(self.ratings_file, delimiter=",", skip_header=1, dtype=float)
        (number_users, number_movies, max_ratings, max_timestamp) = np.max(ratings, axis=0)
        np.random.shuffle(ratings)
        # Divide the data set into train, test and validation set by the ratio 0.7, 0.15, 0.15
        train_set = ratings[0:int((len(ratings) * 0.7))]
        test_set = ratings[(int(len(ratings) * 0.7)):int((len(ratings) * 0.85))]
        validation_set = ratings[int((len(ratings) * 0.85)):]
        # Check that the division results in the appropriate matrices
        assert (len(test_set) + len(train_set) + len(validation_set)) == len(ratings)
        # Construct utility matrix
        utility_matrix = np.empty((int(number_movies), int(number_users)))
        for user, movie, rating, timestamp in train_set:
            utility_matrix[int(movie)-1, int(user)-1] = rating
        # Replace 0 values, needed for later
        for ix, iy in np.ndindex(utility_matrix.shape):
            if utility_matrix[ix, iy] == 0:
                utility_matrix[ix, iy] = np.nan
        print("finished constructing the utility matrix")
        np.save(self.train_file_name, train_set)
        np.save(self.test_file_name, test_set)
        np.save(self.validation_file_name, validation_set)
        np.save(self.utility_file_name, utility_matrix)
        return (train_set, test_set, validation_set, utility_matrix)

    def __check_files(self) -> bool:
        """A private method used to check if the numpy matrices already exist in the given directory

        Returns:
            Bool: True if the matrices file exist, otherwise false
        """ 
        if (os.path.isfile(self.train_file_name) and os.path.isfile(self.test_file_name) 
        and os.path.isfile(self.validation_file_name) and os.path.isfile(self.utility_file_name)):
            return True

        return False
