def test_column_names(clean_data):
    expected_colums = ['age',
                       'workclass',
                       'fnlgt',
                       'education',
                       'marital_status',
                       'occupation',
                       'relationship',
                       'race',
                       'sex',
                       'hours_per_week',
                       'native_country',
                       'salary']

    these_columns = clean_data.columns.values

    # This also enforces the same order
    assert list(expected_colums) == list(these_columns)


def test_row_count(clean_data):
    assert 15000 < clean_data.shape[0] < 1000000
