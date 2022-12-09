import json

if __name__ == '__main__':

    # reading data
    with open('test_1.json', 'r') as input_file:
        raw_data = json.load(input_file)

    # taking only what we neet from the raw data and structuring it as we need
    result_data = list()
    skip_counter = 0
    for i, sample in enumerate(raw_data):
        try:
            result_data.append((
                    sample['text'], {'entity': tuple((entity['start'], entity['end'], entity['labels'][0])
                                                     for entity in sample['class'])}
            ))
        except KeyError as err:
            print(f'There is no field {err} in the {i+1} line')

    # write result to file
    with open('result.json', 'w') as output_file:
        output_file.write(json.dumps(result_data, indent=4))