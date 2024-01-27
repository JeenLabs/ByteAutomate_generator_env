import os


class EnvFileManager:
    ENV_FILE_NAME = '.env'

    @classmethod
    def save_to_env_file(cls, key, value):
        env_data = {}  # To store key-value pairs from the existing .env file

        # Check if the .env file exists
        if os.path.isfile(cls.ENV_FILE_NAME):
            with open(cls.ENV_FILE_NAME, 'r') as file:
                # Read existing key-value pairs from the .env file
                for line in file:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        parts = line.split('=')
                        if len(parts) == 2:
                            env_data[parts[0]] = parts[1]

        # Update the value of the key or append a new line if the key doesn't exist
        env_data[key] = value

        # Write the updated key-value pairs back to the .env file
        with open(cls.ENV_FILE_NAME, 'w') as file:
            file.write("# This is a ByteAutomate .env file\n")
            for k, v in env_data.items():
                file.write(f"{k}={v}\n")

    @classmethod
    def main(cls):
        predefine_keys = ["DatabaseName", "DatabasePath"]
        for key in predefine_keys:
            value = input(f"Enter the value for '{key}' : ")
            cls.save_to_env_file(key, value)
            print(f"Environment variable '{key}' with value '{
                  value}' saved to {cls.ENV_FILE_NAME}")


# Run the program
# EnvFileManager.main()
