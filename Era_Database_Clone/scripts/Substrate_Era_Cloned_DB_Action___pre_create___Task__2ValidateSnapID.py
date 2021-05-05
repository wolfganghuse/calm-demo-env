# Set creds and headers
era_user = '@@{era_creds.username}@@'
era_pass = '@@{era_creds.secret}@@'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

# Get Time Machine Capability
url  = "https://@@{era_ip}@@:8443/era/v0.8/tms/@@{TM_ID}@@/capability?summary=false&time-zone=UTC"
resp = urlreq(url, verb='GET', auth='BASIC', user=era_user, passwd=era_pass, headers=headers)

if resp.ok:
  
  # If the SnapshotID macro is empty, we need to grab the last snap
  if "@@{source_snapshot_id}@@" == "":
  
    # Cycle through the snapshot modes
    for modes in json.loads(resp.content)['capability']:

      # We only care about the recent "Continuous" snapshots
      if modes['mode'] == "CONTINUOUS":
        
        # If there are no snapshots, error out
        if not modes['snapshots']:
          print "ERROR: You must either provide a Snapshot ID, OR have a Continuous Snapshot."
          exit(1)
          
        # Else, grab the last Snapshot ID and exit success
        else:
          print "VALIDATED_SNAP_ID={0}".format(modes['snapshots'][len(modes['snapshots'])-1]['id'])
          exit(0)
      
  # If the snapshot macro is not empty, we need to check that it's a valid snap ID
  else:
    
    # Cycle through the snapshot modes
    for modes in json.loads(resp.content)['capability']:
      
      # Cycle through the snapshots if they exist
      if modes['snapshots']:
        for snapshot in modes['snapshots']:
          
          # If the SnapshotID macro equals an actual Snap ID, then print out and exit success
          if snapshot['id'] == "@@{source_snapshot_id}@@":
            print "VALIDATED_SNAP_ID={0}".format(snapshot['id'])
            exit(0)
          
    # If we've gotten to this point, the SnapshotID macro is not a valid Snap ID, so error out
    print "ERROR: The Snapshot ID you entered is not valid. You must either:"
    print "  1. Provide a valid Snapshot ID from the list below, or"
    print "  2. Leave the SnapshotID field blank to use the last Snapshot."
    print "  ========================"

    # Cycle through the snapshot modes
    for modes in json.loads(resp.content)['capability']:
      print "{0} MODE".format(modes['mode'])
    
      # Cycle through the snapshots if they exist
      if modes['snapshots']:
        for snapshot in modes['snapshots']:
          print "  ------------------------"
          print "  Snapshot ID (copy this): {0}".format(snapshot['id'])
          print "  Snapshot Time Stamp:     {0}".format(snapshot['snapshotTimeStamp'])
        
      # Print message if the don't exist
      else:
        print "  ------------------------"
        print "  No {0} snapshots exist.".format(modes['mode'].lower())

    exit(1)
  
  # If we've gotten this far, something unknown went wrong
  print "Unknown error.  Please contact your Administrator."
  exit(1)

# In the event something went wrong with the API call
else:
  print "Get Time Machine Capability request failed", json.dumps(json.loads(resp.content), indent=4)
  exit(1)