from prodigy.components.db import connect

examples = [{"text": "hello world", "_task_hash": 123, "_input_hash": 456}]

db = connect()                                     # uses settings from prodigy.json
db.add_dataset("test_dataset")                     # add dataset
assert "test_dataset" in db                        # check that dataset was added
db.add_examples(examples, ["test_dataset"])        # add examples to dataset
examples = db.get_dataset_examples("test_dataset") # retrieve a dataset's examples
assert len(examples) == 1 
