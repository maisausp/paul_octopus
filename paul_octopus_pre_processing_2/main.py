import read.read_data as read_data
import compile_dataset.compile_dataset as compiler
import write.write_dataset as writer

v_path_datasets = 'datasets/just_participants/'

def generate_features_dataset():
    raw_data = read_data.read_historical_results()

    dataset_train, dataset_test, dataset_2022 = compiler.get_train_test_data_sets(raw_data)
    writer.write_datasets(v_path_datasets + 'all_score', dataset_train, dataset_test, dataset_2022)  

    dataset_train_th_4 = compiler.set_score_threshold(dataset_train, v_th_max = 4)
    writer.write_datasets(v_path_datasets + 'th_4', dataset_train_th_4, dataset_test, dataset_2022)  

    dataset_train_no_th_4 = compiler.remove_equal_greater_score(dataset_train_th_4, 4)
    writer.write_datasets(v_path_datasets + 'no_th_4', dataset_train_no_th_4, dataset_test, dataset_2022) 

    dataset_train_no_th_3 = compiler.remove_equal_greater_score(dataset_train_no_th_4, 3)
    writer.write_datasets(v_path_datasets + 'no_th_3', dataset_train_no_th_3, dataset_test, dataset_2022) 

def read_features_dataset():

    dataset_train, dataset_test = read_data.read_train_test_datasets(v_path_datasets + 'all_score')
    dataset_2022 = read_data.read_features_datasets(v_path_datasets + 'all_score')

    writer.plot_histogram_goals(v_path_datasets + 'all_score/data_visualization/train_', dataset_train)
    writer.plot_histogram_goals(v_path_datasets + 'all_score/data_visualization/test_', dataset_test)
    
    print(dataset_2022)
    print(dataset_2022['Brazil'])

if __name__ == '__main__':

    # ToDo: Extrair vitórias e derrotas?
    # ToDo: Extrair estatísticas dos últimos X jogos, independente do oponente?
    # ToDo: Separa perdedores e vencedores? Mas como avaliar as novas amostras?

    
    #generate_features_dataset()
    read_features_dataset()

    print("Terminou")