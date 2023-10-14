def getDataFromRow(df_ptr, rowNum):
    return df_ptr.values.astype(float).tolist()[rowNum-1]