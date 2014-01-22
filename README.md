whatsapp-privacy-version
========================

A collection of scripts to build a more privacy-aware WhatsApp version that doesn't leak your whole address book, but only a selected few contacts that can be manually added.

Based on these tutorials by Nicholas FitzRoy-Dale (lardcave.net):
Part 1 - http://code.lardcave.net/entries/2012/04/07/175843/
Part 2 - http://code.lardcave.net/entries/2012/04/22/135057/

REQUIREMENTS:
1. Installed adb and apktool
2. Created keystore with the name "key.keystore" as per Part 1 of the tutorial
3. Got FakeContract.smali from Part 2 of the Lardcave.net tutorial
4. Placed all these files in the cloned git directory.

CONSIDERATIONS BEFORE USE:
WhatsApp has a way to notice that you tampered with it, and will NOT allow you to register your phone with a modified version.
However, this check is ONLY triggered upon registration, not when you run WhatsApp normally.
So you can install the normal WhatsApp version, block access to your contacts via AppOps, then run WhatsApp and register your phone.
Afterwards, backup the WhatsApp data (i.e. with TitaniumBackup) and remove WhatsApp.
Then follow the procedures below and restore the data after installation of the modified version has finished.

USAGE (also works whenever there is an update to WhatsApp!):
1. Download the WhatsApp APK from the PlayStore. You can use http://apps.evozi.com/apk-downloader/ for this.
2. Save the APK as com.whatsapp-1_orig.apk in the same directory as this script.
3. Run this script while your Android phone is unlocked (such that installation can proceed immediately)

If you encounter any errors, you will probably have to update hack_contacts.py to really catch all calls to the Contacts API.
Send me a pull request for your new version if you did this!
Have fun and happy hacking!

KNOWN BUGS:
The FakeContacts provider sometimes loses contacts arbitrarily. I have no idea why exactly this happens... sorry :( But since your open chats will not be affected, it just means you see no name for that contact anymore.

