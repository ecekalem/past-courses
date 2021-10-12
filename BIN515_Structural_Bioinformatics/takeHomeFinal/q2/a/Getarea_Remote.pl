#!/usr/bin/perl -w
# Instructions: 
# How to Use: perl getarea.pl PDBFILE.pdb 
# Results will be written in PDBFILE.pdb.txt file
# Please feel to modify it based on your requirement.
# Written by Surendra Negi, UTMB Galveston. 
#
use strict;
use LWP;
use LWP::UserAgent;
use HTTP::Request::Common;
use HTTP::Headers;
my $ua = LWP::UserAgent->new();
my $request = HTTP::Request->new();
my $CURRENT_DIR=$ENV{'PWD'};
my $PDBfile = shift;
my $url="http://curie.utmb.edu/cgi-bin/getarea.cgi";
my $name="test" ; # Use any name of choice.. default is test 
my $email = "ssnegi\@utmb.edu";# Please type your email address. e.g myemailID\@MyInstitute.edu
my $probesize = "1.4"; # Water probe
my $gradi= "n";  # (y OR n) if you are interested in gradient calculation
my $output = "2"; # 1= Total Area/Energy, 2 = Area per residue, 3 = Area per atom type, 4 = Area per individual atom type.
my $response = $ua->request(POST $url, Content_Type => 'form-data', 
           Content => [
             'water'  => $probesize,
             'gradient'  =>  $gradi,
             'name' => $name,
             'email' => $email,
             'Method' => $output,
             'PDBfile' => [$PDBfile],
            ],
            );
my $html = $response->content;
open(NEWPDBFILE,">$PDBfile.txt") or dienice(" Can't open PDB file $!");
print NEWPDBFILE "$html\n";
close(NEWPDBFILE);
exit;



