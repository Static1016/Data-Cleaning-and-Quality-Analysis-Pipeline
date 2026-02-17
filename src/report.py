def data_quality_report(mh):
    report = {
        "rows": mh.shape[0],
        "columns": mh.shape[1],
        "missing_values": mh.isnull().sum().sum(),
        "duplicates": mh.duplicated().sum()
    }

    return report