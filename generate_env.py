import os


class EnvFileManager:
    ENV_FILE_NAME = '.env'

    @classmethod
    def save_to_env_file(cls, key, value):
        # Check if the .env file exists, create one if not
        if not os.path.isfile(cls.ENV_FILE_NAME):
            with open(cls.ENV_FILE_NAME, 'w') as file:
                file.write("# This is a ByteAutomate .env file\n")

        # Append the new key-value pair to the .env file
        with open(cls.ENV_FILE_NAME, 'a') as file:
            file.write(f"{key}={value}\n")

    @classmethod
    def main(cls):
        predefinekey = ["DatabaseName", "DatabasePath"]
        for key in predefinekey:
            value = input(f"Enter the value for '{key}' : ")
            cls.save_to_env_file(key, value)
            print(f"Environment variable '{key}' with value '{
                value}' saved to {cls.ENV_FILE_NAME}")


# Run the program
# EnvFileManager.main()
