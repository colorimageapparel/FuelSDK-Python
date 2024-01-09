import FuelSDK

try:
    debug = True
    stubObj = FuelSDK.ET_Client(False, debug)

    NameOfAttribute = "PythonSDKEmail"

    # Create Profile Attribute
    print(">>> Create Profile Attribute")
    postAttribute = FuelSDK.ET_ProfileAttribute()
    postAttribute.auth_stub = stubObj
    postAttribute.props = {"Name": NameOfAttribute, "PropertyType": "string"}
    postResponse = postAttribute.post()
    print("Post Status: " + str(postResponse.status))
    print("Code: " + str(postResponse.code))
    print("Message: " + str(postResponse.message))
    print("Result Count: " + str(len(postResponse.results)))
    print("Results: " + str(postResponse.results))

except Exception as e:
    print("Caught exception: " + e.message)
    print(e)
