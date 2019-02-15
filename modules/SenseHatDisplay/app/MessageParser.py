class MessageParser:
    #Returns the highest probablity tag in the json object (takes the output as json.loads as input)
    def highestProbabilityTagMeetingThreshold(self, allTagsAndProbability, threshold):
        highestProbabilityTag = 'none'
        highestProbability = 0
        #print(allTagsAndProbability)
        for value in allTagsAndProbability['predictions']:
            #print(value['tagName'])
            #print(value['probability'])
            if value['probability'] > highestProbability and value['probability'] > threshold:
                highestProbability=value['probability']
                highestProbabilityTag=value['tagName']
            #if item['Probability'] > highestProbability and item['Probability'] > threshold:
             #   highestProbability = item['Probability']
             #   highestProbabilityTag = item['Tag']
        return highestProbabilityTag