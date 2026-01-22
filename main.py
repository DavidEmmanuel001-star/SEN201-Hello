# main.py
# SDLC Implementation Project
# Author: David Emmanuel Enenche

def requirements_analysis():
    print("\n[Requirements Analysis]")
    print("Identify what the user needs and gather system requirements.")

def system_design():
    print("\n[System Design]")
    print("Design the system architecture and plan the structure of the software.")

def implementation():
    print("\n[Implementation / Coding]")
    print("Write the program code according to the design specifications.")

def testing():
    print("\n[Testing]")
    print("Check the program for errors and ensure it works as expected.")

def deployment():
    print("\n[Deployment]")
    print("Release the software so users can start using it.")

def maintenance():
    print("\n[Maintenance]")
    print("Update and improve the system after deployment.")

def main():
    print("Welcome to the SDLC Demonstration Project!")
    print("This program shows the main phases of the Software Development Life Cycle.\n")

    phases = [
        requirements_analysis,
        system_design,
        implementation,
        testing,
        deployment,
        maintenance
    ]

    for phase in phases:
        input("Press Enter to see the next SDLC phase...")
        phase()

    print("\nAll SDLC phases demonstrated successfully. Thank you!")

if __name__ == "__main__":
    main()
