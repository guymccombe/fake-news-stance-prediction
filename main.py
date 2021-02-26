import pandas as pd

if __name__ == '__main__':
    merged = [None] * 2
    for idx, prefix in enumerate(['train', 'test']):
        body_df = pd.read_csv(f'{prefix}_bodies.csv', index_col=0)
        stance_df = pd.read_csv(f'{prefix}_stances.csv')

        merged_df = pd.merge(stance_df, body_df, on='Body ID')
        merged_df = merged_df.rename(
            columns={'Headline': 'headline', 'Body ID': 'body_id',
                     'Stance': 'stance', 'articleBody': 'body'}
        )
        merged[idx] = merged_df

    train_df, test_df = merged
