def model_output_formatting(prediction):

    if prediction == [1]:

        predicition = 'Hurray you would have most likely survived'

    elif prediction == [1]:

        predicition = 'Unfortunatley it did not look good for you'

    else:

        predicition = 'Error'

    return predicition
