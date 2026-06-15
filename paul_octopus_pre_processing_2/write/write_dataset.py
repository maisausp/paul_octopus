import numpy as np
import os
from matplotlib import pyplot as plt

def write_datasets(p_path, dataset_train, dataset_test, dataset_prediction, p_prediction_dataset_name = 'dataset_2026.txt'):
    
    os.makedirs(p_path + '/feature_vs_label', exist_ok=True)
    
    np.savetxt( p_path + '/dataset_train.txt', dataset_train, delimiter=';')
    np.savetxt( p_path + '/dataset_test.txt', dataset_test, delimiter=';')

    filehandler = open(p_path + '/' + p_prediction_dataset_name, 'wt')
    filehandler.write(str(dataset_prediction))
    filehandler.close()    

    plot_feature_vs_label(p_path + "/feature_vs_label/train_", dataset_train)
    plot_feature_vs_label(p_path + "/feature_vs_label/test_", dataset_test)
    

def plot_feature_vs_label(p_path, p_dataset):
    
    X = p_dataset[:,:-1]
    y = p_dataset[:,-1]

    for i in range(X.shape[1]):

        sizes = np.random.uniform(15, 80, len(X[:,i]))
        colors = np.random.uniform(15, 80, len(X[:,i]))
        fig, ax = plt.subplots()
        ax.hist2d(X[:,i], y)

        plt.title('Feature vs Label')
        plt.ylabel('Número gols')  
        plt.xlabel('Feature' + str(i))
        plt.show()
        plt.savefig(p_path + str(i) + "_feature.png", format="PNG")
        plt.close()

def plot_histogram_goals(p_path, p_dataset):
    y = p_dataset[:,-1]
    n, bins, patches = plt.hist(y)
    plt.xticks(bins)
    plt.yticks([])
    # plot values on top of bars
    for idx, value in enumerate(n):
        if value > 0:
            plt.text(bins[idx], value+5, int(value), ha='center')

    plt.xlabel("Magnitude")
    plt.ylabel("Frequency")
    plt.show()
    plt.savefig(p_path + "_histogram.png", format="PNG")
    plt.close()
