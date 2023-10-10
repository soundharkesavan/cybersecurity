import pyotp
import qrcode
import time

while True:
    # Generate a new random secret key for each iteration
    key = pyotp.random_base32()
    totp = pyotp.TOTP(key)

    # Generate the provisioning URI and save it as a QR code
    uri = totp.provisioning_uri(name="soundhar", issuer_name="soundhar App")
    qrcode.make(uri).save("pass.png")
    print("QR code updated. Please scan the new QR code.")

    # Wait for 10 seconds before updating the QR code again
    time.sleep(10)

    input_code = input("Enter code (or type 'exit' to quit):")

    if input_code.lower() == 'exit':
        print("Exiting the program.")
        break

    try:
        verification_result = totp.verify(input_code)
        if verification_result:
            print("Code is valid.")
        else:
            print("Code is invalid.")
    except pyotp.utils.PyOTPError as e:
        print(f"Error: {str(e)}")
