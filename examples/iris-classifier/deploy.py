import promote
from schema import Schema #https://pypi.python.org/pypi/schema

import helpers
# load in our saved model weights
from sklearn.externals import joblib
WEIGHTS = joblib.load('./objects/model_weights.pkl')

# instanciate the Promote class with our API information
p = promote.Promote("colin", "789asdf879h789a79f79sf79s", "https://sandbox.c.yhat.com/")

#validate that we only process data that has ints and floats
@promote.validate_json(Schema([[int, float]]))
def promoteModel(data):
    prediction = helpers.getclass.get_classname(WEIGHTS.predict(data).tolist())
    return {"prediction": prediction}

# Add two flowers as test data
TESTDATA = [[5.1, 3.5, 1.4, 0.2], [6.7, 3.1, 5.6, 2.4]]
promoteModel(TESTDATA)

# name and deploy our model
p.deploy("IrisClassifier", promoteModel, TESTDATA, confirm=True, dry_run=True, verbose=0)

# once our model is deployed and online, we can send data and recieve predictions
# p.predict("IrisClassifier", TESTDATA)