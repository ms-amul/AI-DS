def chatbot():
    while True:
        user_input = input("Enter your message: ")
        if user_input == "Hi" or user_input == "hi":
            print("Hello")
        elif user_input == "Bye" or user_input == "bye":
            print("Goodbye")
            break
        elif user_input == "1":
            print(
                "A snoozing laptop can mean that the battery is dead. Consider plugging in the laptop and trying again." +

                "When the laptop has trouble waking from Sleep mode — and you have to turn it off and then turn it on "
                "again to regain control — you have a problem with the power management system in your laptop.")
        elif user_input == "2":
            print(
                "Batteries die. Even the modern smart batteries are good for only so long. When your battery goes, "
                "replace it with a new one — if you can. Most modern laptops, especially the 2-in-1 tablet PCs, "
                "do not sport removable batteries. In that case, you must replace the laptop.")



        elif user_input == "3":
            print(
                "Some laptop touch pads seem to operate merely by looking at them. Rather than be frustrated by these "
                "touchy touch pads, simply adjust the touch pad’s sensitivity. Follow these steps: "

                "Open the Control Panel." +

                "Press Win+X to bring up the supersecret menu. Choose Control Panel." +

                "Beneath the Hardware and Sound heading, click the View Devices and Printers link." +

                "Right-click your laptop’s icon." +

                "A shortcut menu appears, listing hardware items associated with your laptop." +

                "Choose Mouse Settings." +

                "The Mouse Properties dialog box appears." +

                "Use the Mouse Properties dialog box to review touch pad settings. You should find a Touchpad tab: "
                "Click that tab. If a Settings button is available, click it. You should arrive at a window where you "
                "can adjust the touch pad’s sensitivity." +

                "Lamentably, not every laptop’s touch pad features a specialized dialog box." +

                "Mouse features can also be adjusted in the Settings app: Click Devices, and then choose Mouse & "
                "Touchpad on the left side of the window.")

        elif user_input == "4":
            print("Keyboard problems happen more often than you would imagine. The solution is generally simple: You "
                  "accidentally press the Num Lock key on the laptop’s keyboard, and half the alphabet keys on your "
                  "keyboard start acting like numbers. "

                  "The solution is to press the Num Lock key and restore your keyboard to full alphabetic operation.")

        elif user_input == "5":
            print(
                "When your laptop suddenly loses its ability to sleep or to enter Hibernate mode, it means that you "
                "might have a problem with its power management hardware or software. "

                "First, check your computer manufacturer’s web page to see whether you can find additional "
                "information or software updates. "

                "Second, ensure that power management is properly enabled."

                "Finally, confirm that other hardware or software isn’t interfering with the power management "
                "software. If so, "
                "remove the interfering software or hardware or check for updates that don’t mess with your "
                "laptop’s power management system. A good trick to try is System Restore, just in case a recent "
                "update messed with the laptop’s power management software.")
        else:
            print("Invalid message")

print("Hi I am chatbot of HP service company")
print("1.My laptop won’t wake up")
print("2.The battery won’t charge")
print("3.Touch pad")
print("4.keyboard")
print("5.Power management ")
chatbot()
