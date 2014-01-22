#!/bin/bash
#
# WhatsApp, FakeContacts version install script by Natanji
#

echo "Unpacking com.whatsapp-1_orig.apk..." 
apktool d -f com.whatsapp-1_orig.apk apk ||
    {
        echo "Error unpacking. Perhaps com.whatsapp-1_orig.apk is missing?";
        exit 1
    } 
echo "Unpacking successful. Patching..."
python2 ./hack_contacts.py
REMAINING=`grep -r 'android.provider.ContactsContract.*_URI' apk/smali/`
REMAINING_NUM=$(echo $REMAINING | wc -l)
if [ $REMAINING_NUM -le 1 ];
then
    echo "Successfully patched everything. Injecting FakeContacts API..."
    {
        mkdir -p apk/smali/net/lardcave/fakecontacts &&
        cp FakeContract.smali apk/smali/net/lardcave/fakecontacts;
    } &&
    {
        "Injection completed. Packing..."
        apktool b apk com.whatsapp-1.apk;
    } &&
    {
        echo "Packing completed. Signing..."
        jarsigner -keystore key.keystore com.whatsapp-1.apk key;
    } &&
    {
        echo "Signing successful. Installing..."
        adb install -r com.whatsapp-1.apk;
    } &&
    { 
        echo "Done."
        exit 0;
    }
    echo "An error occured. Sorry :("
    exit 1
else
    echo "Could not patch out all instances of the Contacts API."
    echo "Instances still remaining:"
    echo $REMAINING
    echo "Please check them manually and add them to hack_contacts.py for next time!"
    exit 1
fi

