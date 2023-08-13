# Author: Sakthi Santhosh
# Created on: 13/08/2023
#
# Flask App Runner
def main():
    from app import app_handle

    app_handle.run(debug=True, host="0.0.0.0")

if __name__ == "__main__":
    main()
