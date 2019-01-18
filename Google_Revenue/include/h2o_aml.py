import h2o
from h2o.automl import H2OAutoML

h2o.connect()

path = '/Users/abhaysinghal/Documents/Kaggle/Revenue/'

train = h2o.import_file('/Users/abhaysinghal/Documents/Kaggle/Revenue/features.csv')

i = 1+'crash'

train = train.drop(['fullVisitorId', 'sessionId', 'gclId', 'visitId', 'visitNumber', 'visitStartTime'])
y = 'total'

train2, valid = train.split_frame(ratios=[0.8])

aml = H2OAutoML(max_runtime_secs=120)
aml.train(training_frame=train2, validation_frame=valid, y=y)
model_path = h2o.save_model(aml.leader, path=path)

test = h2o.import_file('/Users/abhaysinghal/Documents/Kaggle/Revenue/test_set.csv')
preds = aml.leader.predict(test)
h2o.download_csv(preds, path + 'aml_preds_1.csv')