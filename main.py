import mlflow
import argparse


def main(training= True):
    with mlflow.start_run() as run:
        if training:
            print('###### TRAINING ######')
            mlflow.run('.', 'stage01', use_conda=False)
            mlflow.run('.', 'stage02', use_conda=False)
            mlflow.run('.', 'stage03', use_conda=False)
        else:
            print('###### PREDICTING ######')
            mlflow.run('.', 'stage01', use_conda=False)
            mlflow.run('.', 'stage03', use_conda=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--training', '-t', type= int, default=0, help='Train the model')
    parsed_args = parser.parse_args()
    print(f'Training: {parsed_args.training}')
    main(training=parsed_args.training)
