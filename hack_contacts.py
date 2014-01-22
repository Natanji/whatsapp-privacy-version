#!/usr/bin/python2
#
# Original script by Nicholas FitzRoy-Dale (lardcave.net)
# Modified by Natanji
#

import os

REPLACEMENTS = {
		'Landroid/provider/ContactsContract$RawContacts;->CONTENT_URI:':
			'Lnet/lardcave/fakecontacts/FakeContract;->RAW_CONTACTS_CONTENT_URI:',

		'Landroid/provider/ContactsContract$Contacts;->CONTENT_FILTER_URI:':
			'Lnet/lardcave/fakecontacts/FakeContract;->CONTACTS_CONTENT_FILTER_URI:',
			
		'Landroid/provider/ContactsContract$Contacts;->CONTENT_URI:':
			'Lnet/lardcave/fakecontacts/FakeContract;->CONTACTS_CONTENT_URI:',

		'Landroid/provider/ContactsContract$Data;->CONTENT_URI:':
			'Lnet/lardcave/fakecontacts/FakeContract;->DATA_CONTENT_URI:',

		'Landroid/provider/ContactsContract$CommonDataKinds$Phone;->CONTENT_URI:':
			'Lnet/lardcave/fakecontacts/FakeContract;->CDK_PHONE_CONTENT_URI:',

		'Landroid/provider/ContactsContract$PhoneLookup;->CONTENT_FILTER_URI:':
			'Lnet/lardcave/fakecontacts/FakeContract;->PHONELOOKUP_CONTENT_FILTER_URI:',

		'Landroid/provider/ContactsContract$RawContacts;->getContactLookupUri(':
			'Lnet/lardcave/fakecontacts/FakeContract;->RawContacts_getContactLookupUri(',

		'Landroid/provider/ContactsContract$Contacts;->CONTENT_VCARD_URI:':
			'Lnet/lardcave/fakecontacts/FakeContract;->CONTACTS_CONTENT_VCARD_URI:',

		'Landroid/provider/ContactsContract$Contacts;->getLookupUri(':
			'Lnet/lardcave/fakecontacts/FakeContract;->Contacts_getLookupUri(',

        #added later
        'Landroid/provider/ContactsContract$Profile;->CONTENT_URI:':
            'Lnet/lardcave/fakecontacts/FakeContract;->CONTACTS_CONTENT_URI:',

        'Landroid/provider/ContactsContract$AggregationExceptions;->CONTENT_URI:':
            'Lnet/lardcave/fakecontacts/FakeContract;->CONTACTS_CONTENT_URI:',

        'Landroid/provider/ContactsContract$CommonDataKinds$Email;->CONTENT_URI:':
            'Lnet/lardcave/fakecontacts/FakeContract;->CONTACTS_CONTENT_URI:',

        'Landroid/provider/ContactsContract$CommonDataKinds$StructuredPostal;->CONTENT_URI:':
            'Lnet/lardcave/fakecontacts/FakeContract;->CONTACTS_CONTENT_URI:',
            
            
            
}

def getfiles():
	filelist = []

	def callback(arg, dirname, files):
		filelist.extend(os.path.join(dirname, filename) for filename in files if filename.endswith('.smali'))
	
	os.path.walk('apk/smali', callback, None)
	return filelist

def rewrite(filename):
	with open(filename, 'rb') as handle:
		data = handle.read()

	for repl in REPLACEMENTS.keys():
		data = data.replace(repl, REPLACEMENTS[repl])
	
	with open(filename, 'wb') as handle:
		handle.write(data)

for filename in getfiles():
	rewrite(filename)

