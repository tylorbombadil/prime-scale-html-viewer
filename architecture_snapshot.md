# Project Architecture Snapshot

## Directory Tree

**.** _(Full Path: `/home/mint/prime-scale-html-viewer`)_

├── **.git/**
│   ├── `COMMIT_EDITMSG`
│   ├── `HEAD`
│   ├── **branches/**
│   ├── `config`
│   ├── `description`
│   ├── **hooks/**
│   │   ├── `applypatch-msg.sample`
│   │   ├── `commit-msg.sample`
│   │   ├── `fsmonitor-watchman.sample`
│   │   ├── `post-update.sample`
│   │   ├── `pre-applypatch.sample`
│   │   ├── `pre-commit.sample`
│   │   ├── `pre-merge-commit.sample`
│   │   ├── `pre-push.sample`
│   │   ├── `pre-rebase.sample`
│   │   ├── `pre-receive.sample`
│   │   ├── `prepare-commit-msg.sample`
│   │   ├── `push-to-checkout.sample`
│   │   └── `update.sample`
│   ├── `index`
│   ├── **info/**
│   │   └── `exclude`
│   ├── **logs/**
│   │   ├── `HEAD`
│   │   └── **refs/**
│   │       ├── **heads/**
│   │       │   └── `master`
│   │       └── **remotes/**
│   │           └── **origin/**
│   │               └── `master`
│   ├── **objects/**
│   │   ├── **04/**
│   │   │   └── `2745d29e29508cc41dba849f804ff25451cd84`
│   │   ├── **0a/**
│   │   │   └── `3f92fddd41c70e0039fde49622c6a1250c11f6`
│   │   ├── **0e/**
│   │   │   ├── `a90af9f2d40e308382b982ab420a4fefff00d3`
│   │   │   └── `c709a8b268daa58913ea45af8a893b2150070a`
│   │   ├── **14/**
│   │   │   └── `b4cc03c6b4772d8ceafe17b7797bb0b590e389`
│   │   ├── **15/**
│   │   │   └── `031cc30083a6d3740c2ba9ce33c83dc6436ea2`
│   │   ├── **18/**
│   │   │   └── `678405b19a7606972392d70d980bb7e08e1ca0`
│   │   ├── **1c/**
│   │   │   └── `856998103d80179bb594eaed14180a156407b6`
│   │   ├── **21/**
│   │   │   └── `f96f7f09a15d87e1e740c4b72bf8c5ef95f3d8`
│   │   ├── **27/**
│   │   │   └── `35a363470c6156c4dcfd0e76b398bc1d4af8e8`
│   │   ├── **28/**
│   │   │   └── `fac87bf17d33ae325819cbd2c57ce4913c3127`
│   │   ├── **30/**
│   │   │   └── `5c76812aba20aaaf12327999387605e894547f`
│   │   ├── **36/**
│   │   │   └── `fc2fe0ef235ad586eaf813cd322195de83285d`
│   │   ├── **37/**
│   │   │   └── `a9c3df5f385eadec99607a3223cbae4df4c8ae`
│   │   ├── **3e/**
│   │   │   └── `74706b6eb5c525eabd85358edf749d03450cc2`
│   │   ├── **45/**
│   │   │   └── `72e5544d3075d5e636ec8414e133b5840dfe27`
│   │   ├── **4c/**
│   │   │   └── `977944eac86393c14a36cca446a0d0735d2f5b`
│   │   ├── **4d/**
│   │   │   └── `e7cc3d655360c75693cbd2fbc4ed08a3c3a786`
│   │   ├── **51/**
│   │   │   └── `1316580ef1f87b37db5fdd7fcb8f4e26c25fb8`
│   │   ├── **5d/**
│   │   │   ├── `80c5277f177fb1c35818e45d6c24c6d918d95d`
│   │   │   └── `cd5e8ab751a5c29987181a133865c5248f7fba`
│   │   ├── **74/**
│   │   │   └── `33cc3417c7d28a9e0e4ef2742b31f9df30c17d`
│   │   ├── **78/**
│   │   │   └── `000a90e01fb601edd47da2365cf70c98dba9f1`
│   │   ├── **7a/**
│   │   │   └── `e723660a9cabe684cb3919106dfa35c8c6359a`
│   │   ├── **7e/**
│   │   │   └── `608ad65574dd4e9e70521f0c347c8aa71f3078`
│   │   ├── **83/**
│   │   │   └── `72cc9657f94d41b8211ee3ad52dd45748acfd4`
│   │   ├── **84/**
│   │   │   └── `f89988c565fede5c3ea060121f7c23375bd915`
│   │   ├── **8a/**
│   │   │   ├── `7a05a96234e3afd60d618471d1caece3b770f9`
│   │   │   ├── `b6ee2e94d9b1d47b8d2f191b29e28c83eb3cf1`
│   │   │   └── `f33ee556e7fd9e216e3f2a4d8fd820a53e90d4`
│   │   ├── **8b/**
│   │   │   └── `58621f9fac234549bc6c2a15424bb613dbfeaf`
│   │   ├── **8e/**
│   │   │   └── `a0153d12c78ca8bfa9ee411d86611df7ffea89`
│   │   ├── **95/**
│   │   │   └── `d496cc937627a0fcd2cba3877fadd7fa78835c`
│   │   ├── **99/**
│   │   │   └── `6f282475010b04af41b4c80477c7833ff8867a`
│   │   ├── **9a/**
│   │   │   └── `7ee652bf4ba6344d16aadf83a803629f9b1208`
│   │   ├── **9f/**
│   │   │   └── `343eabff9c4b99fc480d3a1924036df08f0822`
│   │   ├── **a0/**
│   │   │   └── `d40bef4daa34abada35b1859072a4a801e926e`
│   │   ├── **a5/**
│   │   │   └── `f7d9775ac832fa4fd5c2a97cb344e5c2ae44b6`
│   │   ├── **af/**
│   │   │   └── `dccddfe5f2ae7a64d508a9b485948c5edc68f0`
│   │   ├── **be/**
│   │   │   └── `586443efd85dbc0c853b4184e1e2527dc3c79a`
│   │   ├── **c0/**
│   │   │   └── `328fea381a2d199e165c261a288b9b2a6c0f1a`
│   │   ├── **c3/**
│   │   │   └── `29cfe77a206ed23f6c25eadf82d8b2bf08667e`
│   │   ├── **d4/**
│   │   │   └── `cd8574bc671f903e6ea2a73e3bf73e7f42dc4e`
│   │   ├── **d9/**
│   │   │   └── `a34e35211d2cb11607a4b829755ede66e5cb40`
│   │   ├── **e6/**
│   │   │   └── `9de29bb2d1d6434b8b29ae775ad8c2e48c5391`
│   │   ├── **e8/**
│   │   │   └── `d66718d01518759dccbaf41f562777919a7bee`
│   │   ├── **ea/**
│   │   │   └── `74ef22ce2c2ba39c64555251381df317a5155d`
│   │   ├── **ec/**
│   │   │   └── `697341e507efd7756cc378cd93c079f2b2e9f8`
│   │   ├── **ed/**
│   │   │   └── `8ab122ed5d96c1c788e12aa9f0ef20494e55ab`
│   │   ├── **f8/**
│   │   │   └── `b9befef86ef06ea088ac1e3e9f58ff97fc0aed`
│   │   ├── **info/**
│   │   └── **pack/**
│   └── **refs/**
│       ├── **heads/**
│       │   └── `master`
│       ├── **remotes/**
│       │   └── **origin/**
│       │       └── `master`
│       └── **tags/**
├── `index.html`
├── **output/**
│   ├── `architecture_snapshot.md`
│   ├── `gap_scout_match_5_notes.json`
│   ├── `log_prime_scale_13_valley.json`
│   ├── `log_prime_scale_3_valley.json`
│   ├── `log_prime_scale_6_peak.json`
│   ├── `log_prime_scale_6_valley.json`
│   ├── `manifest.json`
│   ├── `pure_prime_scale_128_primes.json`
│   ├── `sample_scale.json`
│   ├── `terrain_scale_5_valley.json`
│   ├── `terrain_scale_8_valley.json`
│   └── `terrain_scale_{num_notes}_{mode}.json`
├── **readmes/**
│   ├── `code_paste_template.md`
│   ├── `final_architecture_README.md`
│   ├── `nextgen_README_consolidated.md`
│   ├── `prime_scale_cheatsheet_fullpath.txt`
│   └── `prime_scale_drive_scripts_README.md`
├── `script_prompt.py`
├── **scripts/**
│   ├── `__init__.py`
│   ├── **__pycache__/**
│   │   ├── `__init__.cpython-310.pyc`
│   │   ├── `core_pure_prime_scale.cpython-310.pyc`
│   │   ├── `core_terrain_scale.cpython-310.pyc`
│   │   ├── `core_terrain_scale_modified.cpython-310.pyc`
│   │   ├── `gap_threshold_scout.cpython-310.pyc`
│   │   ├── `main.cpython-310.pyc`
│   │   └── `scale_utils.cpython-310.pyc`
│   ├── `architecture_snapshot.md`
│   ├── `binary_gap_analyzer.py`
│   ├── `cluster_finder.py`
│   ├── `core_pure_prime_scale.py`
│   ├── `core_terrain_scale.py`
│   ├── `core_terrain_scale_final.py`
│   ├── `core_terrain_scale_modified.py`
│   ├── `gap_threshold_scout.py`
│   ├── `main.py`
│   └── `scale_utils.py`
└── `viewer.js`

---

## Project Architecture Snapshot

**/home/mint/prime-scale-html-viewer**

        **.git/**

            `.git/COMMIT_EDITMSG`
            ```
            Updated viewer with graphcal number line and dropdown menu that lists all of the available jsons.
            ```

            `.git/HEAD`
            ```
            ref: refs/heads/master
            ```

            **.git/branches/**

            `.git/config`
            ```
            [core]
            	repositoryformatversion = 0
            	filemode = true
            	bare = false
            	logallrefupdates = true
            [remote "origin"]
            	url = git@github.com:tylorbombadil/prime-scale-html-viewer.git
            	fetch = +refs/heads/*:refs/remotes/origin/*
            [branch "master"]
            	remote = origin
            	merge = refs/heads/master
            ```

            `.git/description`
            ```
            Unnamed repository; edit this file 'description' to name the repository.
            ```

            **.git/hooks/**

                `.git/hooks/applypatch-msg.sample`
                ```sample
                #!/bin/sh
                #
                # An example hook script to check the commit log message taken by
                # applypatch from an e-mail message.
                #
                # The hook should exit with non-zero status after issuing an
                # appropriate message if it wants to stop the commit.  The hook is
                # allowed to edit the commit message file.
                #
                # To enable this hook, rename this file to "applypatch-msg".
                
                . git-sh-setup
                commitmsg="$(git rev-parse --git-path hooks/commit-msg)"
                test -x "$commitmsg" && exec "$commitmsg" ${1+"$@"}
                :
                ```

                `.git/hooks/commit-msg.sample`
                ```sample
                #!/bin/sh
                #
                # An example hook script to check the commit log message.
                # Called by "git commit" with one argument, the name of the file
                # that has the commit message.  The hook should exit with non-zero
                # status after issuing an appropriate message if it wants to stop the
                # commit.  The hook is allowed to edit the commit message file.
                #
                # To enable this hook, rename this file to "commit-msg".
                
                # Uncomment the below to add a Signed-off-by line to the message.
                # Doing this in a hook is a bad idea in general, but the prepare-commit-msg
                # hook is more suited to it.
                #
                # SOB=$(git var GIT_AUTHOR_IDENT | sed -n 's/^\(.*>\).*$/Signed-off-by: \1/p')
                # grep -qs "^$SOB" "$1" || echo "$SOB" >> "$1"
                
                # This example catches duplicate Signed-off-by lines.
                
                test "" = "$(grep '^Signed-off-by: ' "$1" |
                	 sort | uniq -c | sed -e '/^[ 	]*1[ 	]/d')" || {
                	echo >&2 Duplicate Signed-off-by lines.
                	exit 1
                }
                ```

                `.git/hooks/fsmonitor-watchman.sample`
                ```sample
                #!/usr/bin/perl
                
                use strict;
                use warnings;
                use IPC::Open2;
                
                # An example hook script to integrate Watchman
                # (https://facebook.github.io/watchman/) with git to speed up detecting
                # new and modified files.
                #
                # The hook is passed a version (currently 2) and last update token
                # formatted as a string and outputs to stdout a new update token and
                # all files that have been modified since the update token. Paths must
                # be relative to the root of the working tree and separated by a single NUL.
                #
                # To enable this hook, rename this file to "query-watchman" and set
                # 'git config core.fsmonitor .git/hooks/query-watchman'
                #
                my ($version, $last_update_token) = @ARGV;
                
                # Uncomment for debugging
                # print STDERR "$0 $version $last_update_token\n";
                
                # Check the hook interface version
                if ($version ne 2) {
                	die "Unsupported query-fsmonitor hook version '$version'.\n" .
                	    "Falling back to scanning...\n";
                }
                
                my $git_work_tree = get_working_dir();
                
                my $retry = 1;
                
                my $json_pkg;
                eval {
                	require JSON::XS;
                	$json_pkg = "JSON::XS";
                	1;
                } or do {
                	require JSON::PP;
                	$json_pkg = "JSON::PP";
                };
                
                launch_watchman();
                
                sub launch_watchman {
                	my $o = watchman_query();
                	if (is_work_tree_watched($o)) {
                		output_result($o->{clock}, @{$o->{files}});
                	}
                }
                
                sub output_result {
                	my ($clockid, @files) = @_;
                
                	# Uncomment for debugging watchman output
                	# open (my $fh, ">", ".git/watchman-output.out");
                	# binmode $fh, ":utf8";
                	# print $fh "$clockid\n@files\n";
                	# close $fh;
                
                	binmode STDOUT, ":utf8";
                	print $clockid;
                	print "\0";
                	local $, = "\0";
                	print @files;
                }
                
                sub watchman_clock {
                	my $response = qx/watchman clock "$git_work_tree"/;
                	die "Failed to get clock id on '$git_work_tree'.\n" .
                		"Falling back to scanning...\n" if $? != 0;
                
                	return $json_pkg->new->utf8->decode($response);
                }
                
                sub watchman_query {
                	my $pid = open2(\*CHLD_OUT, \*CHLD_IN, 'watchman -j --no-pretty')
                	or die "open2() failed: $!\n" .
                	"Falling back to scanning...\n";
                
                	# In the query expression below we're asking for names of files that
                	# changed since $last_update_token but not from the .git folder.
                	#
                	# To accomplish this, we're using the "since" generator to use the
                	# recency index to select candidate nodes and "fields" to limit the
                	# output to file names only. Then we're using the "expression" term to
                	# further constrain the results.
                	if (substr($last_update_token, 0, 1) eq "c") {
                		$last_update_token = "\"$last_update_token\"";
                	}
                	my $query = <<"	END";
                		["query", "$git_work_tree", {
                			"since": $last_update_token,
                			"fields": ["name"],
                			"expression": ["not", ["dirname", ".git"]]
                		}]
                	END
                
                	# Uncomment for debugging the watchman query
                	# open (my $fh, ">", ".git/watchman-query.json");
                	# print $fh $query;
                	# close $fh;
                
                	print CHLD_IN $query;
                	close CHLD_IN;
                	my $response = do {local $/; <CHLD_OUT>};
                
                	# Uncomment for debugging the watch response
                	# open ($fh, ">", ".git/watchman-response.json");
                	# print $fh $response;
                	# close $fh;
                
                	die "Watchman: command returned no output.\n" .
                	"Falling back to scanning...\n" if $response eq "";
                	die "Watchman: command returned invalid output: $response\n" .
                	"Falling back to scanning...\n" unless $response =~ /^\{/;
                
                	return $json_pkg->new->utf8->decode($response);
                }
                
                sub is_work_tree_watched {
                	my ($output) = @_;
                	my $error = $output->{error};
                	if ($retry > 0 and $error and $error =~ m/unable to resolve root .* directory (.*) is not watched/) {
                		$retry--;
                		my $response = qx/watchman watch "$git_work_tree"/;
                		die "Failed to make watchman watch '$git_work_tree'.\n" .
                		    "Falling back to scanning...\n" if $? != 0;
                		$output = $json_pkg->new->utf8->decode($response);
                		$error = $output->{error};
                		die "Watchman: $error.\n" .
                		"Falling back to scanning...\n" if $error;
                
                		# Uncomment for debugging watchman output
                		# open (my $fh, ">", ".git/watchman-output.out");
                		# close $fh;
                
                		# Watchman will always return all files on the first query so
                		# return the fast "everything is dirty" flag to git and do the
                		# Watchman query just to get it over with now so we won't pay
                		# the cost in git to look up each individual file.
                		my $o = watchman_clock();
                		$error = $output->{error};
                
                		die "Watchman: $error.\n" .
                		"Falling back to scanning...\n" if $error;
                
                		output_result($o->{clock}, ("/"));
                		$last_update_token = $o->{clock};
                
                		eval { launch_watchman() };
                		return 0;
                	}
                
                	die "Watchman: $error.\n" .
                	"Falling back to scanning...\n" if $error;
                
                	return 1;
                }
                
                sub get_working_dir {
                	my $working_dir;
                	if ($^O =~ 'msys' || $^O =~ 'cygwin') {
                		$working_dir = Win32::GetCwd();
                		$working_dir =~ tr/\\/\//;
                	} else {
                		require Cwd;
                		$working_dir = Cwd::cwd();
                	}
                
                	return $working_dir;
                }
                ```

                `.git/hooks/post-update.sample`
                ```sample
                #!/bin/sh
                #
                # An example hook script to prepare a packed repository for use over
                # dumb transports.
                #
                # To enable this hook, rename this file to "post-update".
                
                exec git update-server-info
                ```

                `.git/hooks/pre-applypatch.sample`
                ```sample
                #!/bin/sh
                #
                # An example hook script to verify what is about to be committed
                # by applypatch from an e-mail message.
                #
                # The hook should exit with non-zero status after issuing an
                # appropriate message if it wants to stop the commit.
                #
                # To enable this hook, rename this file to "pre-applypatch".
                
                . git-sh-setup
                precommit="$(git rev-parse --git-path hooks/pre-commit)"
                test -x "$precommit" && exec "$precommit" ${1+"$@"}
                :
                ```

                `.git/hooks/pre-commit.sample`
                ```sample
                #!/bin/sh
                #
                # An example hook script to verify what is about to be committed.
                # Called by "git commit" with no arguments.  The hook should
                # exit with non-zero status after issuing an appropriate message if
                # it wants to stop the commit.
                #
                # To enable this hook, rename this file to "pre-commit".
                
                if git rev-parse --verify HEAD >/dev/null 2>&1
                then
                	against=HEAD
                else
                	# Initial commit: diff against an empty tree object
                	against=$(git hash-object -t tree /dev/null)
                fi
                
                # If you want to allow non-ASCII filenames set this variable to true.
                allownonascii=$(git config --type=bool hooks.allownonascii)
                
                # Redirect output to stderr.
                exec 1>&2
                
                # Cross platform projects tend to avoid non-ASCII filenames; prevent
                # them from being added to the repository. We exploit the fact that the
                # printable range starts at the space character and ends with tilde.
                if [ "$allownonascii" != "true" ] &&
                	# Note that the use of brackets around a tr range is ok here, (it's
                	# even required, for portability to Solaris 10's /usr/bin/tr), since
                	# the square bracket bytes happen to fall in the designated range.
                	test $(git diff --cached --name-only --diff-filter=A -z $against |
                	  LC_ALL=C tr -d '[ -~]\0' | wc -c) != 0
                then
                	cat <<\EOF
                Error: Attempt to add a non-ASCII file name.
                
                This can cause problems if you want to work with people on other platforms.
                
                To be portable it is advisable to rename the file.
                
                If you know what you are doing you can disable this check using:
                
                  git config hooks.allownonascii true
                EOF
                	exit 1
                fi
                
                # If there are whitespace errors, print the offending file names and fail.
                exec git diff-index --check --cached $against --
                ```

                `.git/hooks/pre-merge-commit.sample`
                ```sample
                #!/bin/sh
                #
                # An example hook script to verify what is about to be committed.
                # Called by "git merge" with no arguments.  The hook should
                # exit with non-zero status after issuing an appropriate message to
                # stderr if it wants to stop the merge commit.
                #
                # To enable this hook, rename this file to "pre-merge-commit".
                
                . git-sh-setup
                test -x "$GIT_DIR/hooks/pre-commit" &&
                        exec "$GIT_DIR/hooks/pre-commit"
                :
                ```

                `.git/hooks/pre-push.sample`
                ```sample
                #!/bin/sh
                
                # An example hook script to verify what is about to be pushed.  Called by "git
                # push" after it has checked the remote status, but before anything has been
                # pushed.  If this script exits with a non-zero status nothing will be pushed.
                #
                # This hook is called with the following parameters:
                #
                # $1 -- Name of the remote to which the push is being done
                # $2 -- URL to which the push is being done
                #
                # If pushing without using a named remote those arguments will be equal.
                #
                # Information about the commits which are being pushed is supplied as lines to
                # the standard input in the form:
                #
                #   <local ref> <local oid> <remote ref> <remote oid>
                #
                # This sample shows how to prevent push of commits where the log message starts
                # with "WIP" (work in progress).
                
                remote="$1"
                url="$2"
                
                zero=$(git hash-object --stdin </dev/null | tr '[0-9a-f]' '0')
                
                while read local_ref local_oid remote_ref remote_oid
                do
                	if test "$local_oid" = "$zero"
                	then
                		# Handle delete
                		:
                	else
                		if test "$remote_oid" = "$zero"
                		then
                			# New branch, examine all commits
                			range="$local_oid"
                		else
                			# Update to existing branch, examine new commits
                			range="$remote_oid..$local_oid"
                		fi
                
                		# Check for WIP commit
                		commit=$(git rev-list -n 1 --grep '^WIP' "$range")
                		if test -n "$commit"
                		then
                			echo >&2 "Found WIP commit in $local_ref, not pushing"
                			exit 1
                		fi
                	fi
                done
                
                exit 0
                ```

                `.git/hooks/pre-rebase.sample`
                ```sample
                #!/bin/sh
                #
                # Copyright (c) 2006, 2008 Junio C Hamano
                #
                # The "pre-rebase" hook is run just before "git rebase" starts doing
                # its job, and can prevent the command from running by exiting with
                # non-zero status.
                #
                # The hook is called with the following parameters:
                #
                # $1 -- the upstream the series was forked from.
                # $2 -- the branch being rebased (or empty when rebasing the current branch).
                #
                # This sample shows how to prevent topic branches that are already
                # merged to 'next' branch from getting rebased, because allowing it
                # would result in rebasing already published history.
                
                publish=next
                basebranch="$1"
                if test "$#" = 2
                then
                	topic="refs/heads/$2"
                else
                	topic=`git symbolic-ref HEAD` ||
                	exit 0 ;# we do not interrupt rebasing detached HEAD
                fi
                
                case "$topic" in
                refs/heads/??/*)
                	;;
                *)
                	exit 0 ;# we do not interrupt others.
                	;;
                esac
                
                # Now we are dealing with a topic branch being rebased
                # on top of master.  Is it OK to rebase it?
                
                # Does the topic really exist?
                git show-ref -q "$topic" || {
                	echo >&2 "No such branch $topic"
                	exit 1
                }
                
                # Is topic fully merged to master?
                not_in_master=`git rev-list --pretty=oneline ^master "$topic"`
                if test -z "$not_in_master"
                then
                	echo >&2 "$topic is fully merged to master; better remove it."
                	exit 1 ;# we could allow it, but there is no point.
                fi
                
                # Is topic ever merged to next?  If so you should not be rebasing it.
                only_next_1=`git rev-list ^master "^$topic" ${publish} | sort`
                only_next_2=`git rev-list ^master           ${publish} | sort`
                if test "$only_next_1" = "$only_next_2"
                then
                	not_in_topic=`git rev-list "^$topic" master`
                	if test -z "$not_in_topic"
                	then
                		echo >&2 "$topic is already up to date with master"
                		exit 1 ;# we could allow it, but there is no point.
                	else
                		exit 0
                	fi
                else
                	not_in_next=`git rev-list --pretty=oneline ^${publish} "$topic"`
                	/usr/bin/perl -e '
                		my $topic = $ARGV[0];
                		my $msg = "* $topic has commits already merged to public branch:\n";
                		my (%not_in_next) = map {
                			/^([0-9a-f]+) /;
                			($1 => 1);
                		} split(/\n/, $ARGV[1]);
                		for my $elem (map {
                				/^([0-9a-f]+) (.*)$/;
                				[$1 => $2];
                			} split(/\n/, $ARGV[2])) {
                			if (!exists $not_in_next{$elem->[0]}) {
                				if ($msg) {
                					print STDERR $msg;
                					undef $msg;
                				}
                				print STDERR " $elem->[1]\n";
                			}
                		}
                	' "$topic" "$not_in_next" "$not_in_master"
                	exit 1
                fi
                
                <<\DOC_END
                
                This sample hook safeguards topic branches that have been
                published from being rewound.
                
                The workflow assumed here is:
                
                 * Once a topic branch forks from "master", "master" is never
                   merged into it again (either directly or indirectly).
                
                 * Once a topic branch is fully cooked and merged into "master",
                   it is deleted.  If you need to build on top of it to correct
                   earlier mistakes, a new topic branch is created by forking at
                   the tip of the "master".  This is not strictly necessary, but
                   it makes it easier to keep your history simple.
                
                 * Whenever you need to test or publish your changes to topic
                   branches, merge them into "next" branch.
                
                The script, being an example, hardcodes the publish branch name
                to be "next", but it is trivial to make it configurable via
                $GIT_DIR/config mechanism.
                
                With this workflow, you would want to know:
                
                (1) ... if a topic branch has ever been merged to "next".  Young
                    topic branches can have stupid mistakes you would rather
                    clean up before publishing, and things that have not been
                    merged into other branches can be easily rebased without
                    affecting other people.  But once it is published, you would
                    not want to rewind it.
                
                (2) ... if a topic branch has been fully merged to "master".
                    Then you can delete it.  More importantly, you should not
                    build on top of it -- other people may already want to
                    change things related to the topic as patches against your
                    "master", so if you need further changes, it is better to
                    fork the topic (perhaps with the same name) afresh from the
                    tip of "master".
                
                Let's look at this example:
                
                		   o---o---o---o---o---o---o---o---o---o "next"
                		  /       /           /           /
                		 /   a---a---b A     /           /
                		/   /               /           /
                	       /   /   c---c---c---c B         /
                	      /   /   /             \         /
                	     /   /   /   b---b C     \       /
                	    /   /   /   /             \     /
                    ---o---o---o---o---o---o---o---o---o---o---o "master"
                
                
                A, B and C are topic branches.
                
                 * A has one fix since it was merged up to "next".
                
                 * B has finished.  It has been fully merged up to "master" and "next",
                   and is ready to be deleted.
                
                 * C has not merged to "next" at all.
                
                We would want to allow C to be rebased, refuse A, and encourage
                B to be deleted.
                
                To compute (1):
                
                	git rev-list ^master ^topic next
                	git rev-list ^master        next
                
                	if these match, topic has not merged in next at all.
                
                To compute (2):
                
                	git rev-list master..topic
                
                	if this is empty, it is fully merged to "master".
                
                DOC_END
                ```

                `.git/hooks/pre-receive.sample`
                ```sample
                #!/bin/sh
                #
                # An example hook script to make use of push options.
                # The example simply echoes all push options that start with 'echoback='
                # and rejects all pushes when the "reject" push option is used.
                #
                # To enable this hook, rename this file to "pre-receive".
                
                if test -n "$GIT_PUSH_OPTION_COUNT"
                then
                	i=0
                	while test "$i" -lt "$GIT_PUSH_OPTION_COUNT"
                	do
                		eval "value=\$GIT_PUSH_OPTION_$i"
                		case "$value" in
                		echoback=*)
                			echo "echo from the pre-receive-hook: ${value#*=}" >&2
                			;;
                		reject)
                			exit 1
                		esac
                		i=$((i + 1))
                	done
                fi
                ```

                `.git/hooks/prepare-commit-msg.sample`
                ```sample
                #!/bin/sh
                #
                # An example hook script to prepare the commit log message.
                # Called by "git commit" with the name of the file that has the
                # commit message, followed by the description of the commit
                # message's source.  The hook's purpose is to edit the commit
                # message file.  If the hook fails with a non-zero status,
                # the commit is aborted.
                #
                # To enable this hook, rename this file to "prepare-commit-msg".
                
                # This hook includes three examples. The first one removes the
                # "# Please enter the commit message..." help message.
                #
                # The second includes the output of "git diff --name-status -r"
                # into the message, just before the "git status" output.  It is
                # commented because it doesn't cope with --amend or with squashed
                # commits.
                #
                # The third example adds a Signed-off-by line to the message, that can
                # still be edited.  This is rarely a good idea.
                
                COMMIT_MSG_FILE=$1
                COMMIT_SOURCE=$2
                SHA1=$3
                
                /usr/bin/perl -i.bak -ne 'print unless(m/^. Please enter the commit message/..m/^#$/)' "$COMMIT_MSG_FILE"
                
                # case "$COMMIT_SOURCE,$SHA1" in
                #  ,|template,)
                #    /usr/bin/perl -i.bak -pe '
                #       print "\n" . `git diff --cached --name-status -r`
                # 	 if /^#/ && $first++ == 0' "$COMMIT_MSG_FILE" ;;
                #  *) ;;
                # esac
                
                # SOB=$(git var GIT_COMMITTER_IDENT | sed -n 's/^\(.*>\).*$/Signed-off-by: \1/p')
                # git interpret-trailers --in-place --trailer "$SOB" "$COMMIT_MSG_FILE"
                # if test -z "$COMMIT_SOURCE"
                # then
                #   /usr/bin/perl -i.bak -pe 'print "\n" if !$first_line++' "$COMMIT_MSG_FILE"
                # fi
                ```

                `.git/hooks/push-to-checkout.sample`
                ```sample
                #!/bin/sh
                
                # An example hook script to update a checked-out tree on a git push.
                #
                # This hook is invoked by git-receive-pack(1) when it reacts to git
                # push and updates reference(s) in its repository, and when the push
                # tries to update the branch that is currently checked out and the
                # receive.denyCurrentBranch configuration variable is set to
                # updateInstead.
                #
                # By default, such a push is refused if the working tree and the index
                # of the remote repository has any difference from the currently
                # checked out commit; when both the working tree and the index match
                # the current commit, they are updated to match the newly pushed tip
                # of the branch. This hook is to be used to override the default
                # behaviour; however the code below reimplements the default behaviour
                # as a starting point for convenient modification.
                #
                # The hook receives the commit with which the tip of the current
                # branch is going to be updated:
                commit=$1
                
                # It can exit with a non-zero status to refuse the push (when it does
                # so, it must not modify the index or the working tree).
                die () {
                	echo >&2 "$*"
                	exit 1
                }
                
                # Or it can make any necessary changes to the working tree and to the
                # index to bring them to the desired state when the tip of the current
                # branch is updated to the new commit, and exit with a zero status.
                #
                # For example, the hook can simply run git read-tree -u -m HEAD "$1"
                # in order to emulate git fetch that is run in the reverse direction
                # with git push, as the two-tree form of git read-tree -u -m is
                # essentially the same as git switch or git checkout that switches
                # branches while keeping the local changes in the working tree that do
                # not interfere with the difference between the branches.
                
                # The below is a more-or-less exact translation to shell of the C code
                # for the default behaviour for git's push-to-checkout hook defined in
                # the push_to_deploy() function in builtin/receive-pack.c.
                #
                # Note that the hook will be executed from the repository directory,
                # not from the working tree, so if you want to perform operations on
                # the working tree, you will have to adapt your code accordingly, e.g.
                # by adding "cd .." or using relative paths.
                
                if ! git update-index -q --ignore-submodules --refresh
                then
                	die "Up-to-date check failed"
                fi
                
                if ! git diff-files --quiet --ignore-submodules --
                then
                	die "Working directory has unstaged changes"
                fi
                
                # This is a rough translation of:
                #
                #   head_has_history() ? "HEAD" : EMPTY_TREE_SHA1_HEX
                if git cat-file -e HEAD 2>/dev/null
                then
                	head=HEAD
                else
                	head=$(git hash-object -t tree --stdin </dev/null)
                fi
                
                if ! git diff-index --quiet --cached --ignore-submodules $head --
                then
                	die "Working directory has staged changes"
                fi
                
                if ! git read-tree -u -m "$commit"
                then
                	die "Could not update working tree to new HEAD"
                fi
                ```

                `.git/hooks/update.sample`
                ```sample
                #!/bin/sh
                #
                # An example hook script to block unannotated tags from entering.
                # Called by "git receive-pack" with arguments: refname sha1-old sha1-new
                #
                # To enable this hook, rename this file to "update".
                #
                # Config
                # ------
                # hooks.allowunannotated
                #   This boolean sets whether unannotated tags will be allowed into the
                #   repository.  By default they won't be.
                # hooks.allowdeletetag
                #   This boolean sets whether deleting tags will be allowed in the
                #   repository.  By default they won't be.
                # hooks.allowmodifytag
                #   This boolean sets whether a tag may be modified after creation. By default
                #   it won't be.
                # hooks.allowdeletebranch
                #   This boolean sets whether deleting branches will be allowed in the
                #   repository.  By default they won't be.
                # hooks.denycreatebranch
                #   This boolean sets whether remotely creating branches will be denied
                #   in the repository.  By default this is allowed.
                #
                
                # --- Command line
                refname="$1"
                oldrev="$2"
                newrev="$3"
                
                # --- Safety check
                if [ -z "$GIT_DIR" ]; then
                	echo "Don't run this script from the command line." >&2
                	echo " (if you want, you could supply GIT_DIR then run" >&2
                	echo "  $0 <ref> <oldrev> <newrev>)" >&2
                	exit 1
                fi
                
                if [ -z "$refname" -o -z "$oldrev" -o -z "$newrev" ]; then
                	echo "usage: $0 <ref> <oldrev> <newrev>" >&2
                	exit 1
                fi
                
                # --- Config
                allowunannotated=$(git config --type=bool hooks.allowunannotated)
                allowdeletebranch=$(git config --type=bool hooks.allowdeletebranch)
                denycreatebranch=$(git config --type=bool hooks.denycreatebranch)
                allowdeletetag=$(git config --type=bool hooks.allowdeletetag)
                allowmodifytag=$(git config --type=bool hooks.allowmodifytag)
                
                # check for no description
                projectdesc=$(sed -e '1q' "$GIT_DIR/description")
                case "$projectdesc" in
                "Unnamed repository"* | "")
                	echo "*** Project description file hasn't been set" >&2
                	exit 1
                	;;
                esac
                
                # --- Check types
                # if $newrev is 0000...0000, it's a commit to delete a ref.
                zero=$(git hash-object --stdin </dev/null | tr '[0-9a-f]' '0')
                if [ "$newrev" = "$zero" ]; then
                	newrev_type=delete
                else
                	newrev_type=$(git cat-file -t $newrev)
                fi
                
                case "$refname","$newrev_type" in
                	refs/tags/*,commit)
                		# un-annotated tag
                		short_refname=${refname##refs/tags/}
                		if [ "$allowunannotated" != "true" ]; then
                			echo "*** The un-annotated tag, $short_refname, is not allowed in this repository" >&2
                			echo "*** Use 'git tag [ -a | -s ]' for tags you want to propagate." >&2
                			exit 1
                		fi
                		;;
                	refs/tags/*,delete)
                		# delete tag
                		if [ "$allowdeletetag" != "true" ]; then
                			echo "*** Deleting a tag is not allowed in this repository" >&2
                			exit 1
                		fi
                		;;
                	refs/tags/*,tag)
                		# annotated tag
                		if [ "$allowmodifytag" != "true" ] && git rev-parse $refname > /dev/null 2>&1
                		then
                			echo "*** Tag '$refname' already exists." >&2
                			echo "*** Modifying a tag is not allowed in this repository." >&2
                			exit 1
                		fi
                		;;
                	refs/heads/*,commit)
                		# branch
                		if [ "$oldrev" = "$zero" -a "$denycreatebranch" = "true" ]; then
                			echo "*** Creating a branch is not allowed in this repository" >&2
                			exit 1
                		fi
                		;;
                	refs/heads/*,delete)
                		# delete branch
                		if [ "$allowdeletebranch" != "true" ]; then
                			echo "*** Deleting a branch is not allowed in this repository" >&2
                			exit 1
                		fi
                		;;
                	refs/remotes/*,commit)
                		# tracking branch
                		;;
                	refs/remotes/*,delete)
                		# delete tracking branch
                		if [ "$allowdeletebranch" != "true" ]; then
                			echo "*** Deleting a tracking branch is not allowed in this repository" >&2
                			exit 1
                		fi
                		;;
                	*)
                		# Anything else (is there anything else?)
                		echo "*** Update hook: unknown type of update to ref $refname of type $newrev_type" >&2
                		exit 1
                		;;
                esac
                
                # --- Finished
                exit 0
                ```

            **.git/info/**

                `.git/info/exclude`
                ```
                # git ls-files --others --exclude-from=.git/info/exclude
                # Lines that start with '#' are comments.
                # For a project mostly in C, the following would be a good set of
                # exclude patterns (uncomment them if you want to use them):
                # *.[oa]
                # *~
                ```

            **.git/logs/**

                `.git/logs/HEAD`
                ```
                0000000000000000000000000000000000000000 14b4cc03c6b4772d8ceafe17b7797bb0b590e389 mrbean <doodoo> 1747705804 -0500	commit (initial): Initial commit: lagacy core python algorithm testing sandbox for prepairing to trnslate them into js
                14b4cc03c6b4772d8ceafe17b7797bb0b590e389 7ae723660a9cabe684cb3919106dfa35c8c6359a mrbean <doodoo> 1747740395 -0500	commit: Updated viewer with graphcal number line and dropdown menu that lists all of the available jsons.
                ```

                **.git/logs/refs/**

                    **.git/logs/refs/heads/**

                        `.git/logs/refs/heads/master`
                        ```
                        0000000000000000000000000000000000000000 14b4cc03c6b4772d8ceafe17b7797bb0b590e389 mrbean <doodoo> 1747705804 -0500	commit (initial): Initial commit: lagacy core python algorithm testing sandbox for prepairing to trnslate them into js
                        14b4cc03c6b4772d8ceafe17b7797bb0b590e389 7ae723660a9cabe684cb3919106dfa35c8c6359a mrbean <doodoo> 1747740395 -0500	commit: Updated viewer with graphcal number line and dropdown menu that lists all of the available jsons.
                        ```

                    **.git/logs/refs/remotes/**

                        **.git/logs/refs/remotes/origin/**

                            `.git/logs/refs/remotes/origin/master`
                            ```
                            0000000000000000000000000000000000000000 14b4cc03c6b4772d8ceafe17b7797bb0b590e389 mrbean <doodoo> 1747716064 -0500	update by push
                            14b4cc03c6b4772d8ceafe17b7797bb0b590e389 7ae723660a9cabe684cb3919106dfa35c8c6359a mrbean <doodoo> 1747740491 -0500	update by push
                            ```

            **.git/objects/**

                **.git/objects/04/**

                **.git/objects/0a/**

                **.git/objects/0e/**

                **.git/objects/14/**

                **.git/objects/15/**

                **.git/objects/18/**

                **.git/objects/1c/**

                **.git/objects/21/**

                **.git/objects/27/**

                **.git/objects/28/**

                **.git/objects/30/**

                **.git/objects/36/**

                **.git/objects/37/**

                **.git/objects/3e/**

                **.git/objects/45/**

                **.git/objects/4c/**

                **.git/objects/4d/**

                **.git/objects/51/**

                **.git/objects/5d/**

                **.git/objects/74/**

                **.git/objects/78/**

                **.git/objects/7a/**

                **.git/objects/7e/**

                **.git/objects/83/**

                **.git/objects/84/**

                **.git/objects/8a/**

                **.git/objects/8b/**

                **.git/objects/8e/**

                **.git/objects/95/**

                **.git/objects/99/**

                **.git/objects/9a/**

                **.git/objects/9f/**

                **.git/objects/a0/**

                **.git/objects/a5/**

                **.git/objects/af/**

                **.git/objects/be/**

                **.git/objects/c0/**

                **.git/objects/c3/**

                **.git/objects/d4/**

                **.git/objects/d9/**

                **.git/objects/e6/**

                **.git/objects/e8/**

                **.git/objects/ea/**

                **.git/objects/ec/**

                **.git/objects/ed/**

                **.git/objects/f8/**

                **.git/objects/info/**

                **.git/objects/pack/**

            **.git/refs/**

                **.git/refs/heads/**

                    `.git/refs/heads/master`
                    ```
                    7ae723660a9cabe684cb3919106dfa35c8c6359a
                    ```

                **.git/refs/remotes/**

                    **.git/refs/remotes/origin/**

                        `.git/refs/remotes/origin/master`
                        ```
                        7ae723660a9cabe684cb3919106dfa35c8c6359a
                        ```

                **.git/refs/tags/**

        `index.html`
        ```html
        <!DOCTYPE html>
        <html>
        <head>
          <meta charset="UTF-8">
          <title>Prime Scale Viewer</title>
          <style>
            canvas#line-readout {
              width: 100%;
              height: 60px;
              border: 1px solid #ccc;
              display: block;
              margin-top: 20px;
            }
          </style>
        </head>
        <body>
          <h1>Prime Scale Viewer</h1>
          <div id="scale-display">Loading scale...</div>
          <canvas id="line-readout" width="1000" height="60"></canvas>
          <script src="viewer.js"></script>
        </body>
        </html>
        ```

        **output/**

            `output/architecture_snapshot.md`
            ```md
            # Project Architecture Snapshot
            
            ## Directory Tree
            
            **.** _(Full Path: `/home/mint/prime-scale-html-viewer/output`)_
            
            ├── `gap_scout_match_5_notes.json`
            ├── `log_prime_scale_13_valley.json`
            ├── `log_prime_scale_3_valley.json`
            ├── `log_prime_scale_6_peak.json`
            ├── `log_prime_scale_6_valley.json`
            ├── `manifest.json`
            ├── `pure_prime_scale_128_primes.json`
            ├── `sample_scale.json`
            └── `terrain_scale_8_valley.json`
            
            ---
            
            ## Project Architecture Snapshot
            
            **/home/mint/prime-scale-html-viewer/output**
            
                    `gap_scout_match_5_notes.json`
                    ```json
                    {
                      "name": "gap_scout_match_5_notes",
                      "base_frequency": 220.0,
                      "notes": [
                        {
                          "log_position": 0.0,
                          "frequency": 220.0,
                          "midi": 57,
                          "cents_from_base": 0.0,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.07480798051337051,
                          "frequency": 231.70858596251097,
                          "midi": 58,
                          "cents_from_base": 89.76957661604462,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.6107910531958953,
                          "frequency": 335.9611884703146,
                          "midi": 64,
                          "cents_from_base": 732.9492638350744,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.6728648404106712,
                          "frequency": 350.73182965589353,
                          "midi": 65,
                          "cents_from_base": 807.4378084928054,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.7630023064687417,
                          "frequency": 373.34407362361526,
                          "midi": 66,
                          "cents_from_base": 915.60276776249,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.9068881985485664,
                          "frequency": 412.4993146254886,
                          "midi": 68,
                          "cents_from_base": 1088.2658382582797,
                          "prime_sources": []
                        },
                        {
                          "log_position": 1.0,
                          "frequency": 440.0,
                          "midi": 69,
                          "cents_from_base": 1200.0,
                          "prime_sources": []
                        }
                      ]
                    }
                    ```
            
                    `log_prime_scale_13_valley.json`
                    ```json
                    {
                      "name": "log_prime_scale_13_valley",
                      "base_frequency": 220.0,
                      "notes": [
                        {
                          "log_position": 0.029291666666666667,
                          "frequency": 224.5124096554435,
                          "midi": 57,
                          "cents_from_base": 35.15,
                          "prime_sources": [
                            66863,
                            66877,
                            66883,
                            66889
                          ]
                        },
                        {
                          "log_position": 0.12095833333333333,
                          "frequency": 239.24053635066036,
                          "midi": 58,
                          "cents_from_base": 145.15,
                          "prime_sources": [
                            71249,
                            71257,
                            71261,
                            71263,
                            71287
                          ]
                        },
                        {
                          "log_position": 0.17775,
                          "frequency": 248.84605635407974,
                          "midi": 59,
                          "cents_from_base": 213.29999999999998,
                          "prime_sources": [
                            37057,
                            37061,
                            74131,
                            74143,
                            74149
                          ]
                        },
                        {
                          "log_position": 0.25783333333333336,
                          "frequency": 263.0499648117823,
                          "midi": 60,
                          "cents_from_base": 309.40000000000003,
                          "prime_sources": [
                            39181,
                            39191,
                            78341,
                            78347,
                            78367
                          ]
                        },
                        {
                          "log_position": 0.363375,
                          "frequency": 283.0150009385238,
                          "midi": 61,
                          "cents_from_base": 436.05,
                          "prime_sources": [
                            42157,
                            84299,
                            84307,
                            84313,
                            84317,
                            84319
                          ]
                        },
                        {
                          "log_position": 0.3879166666666667,
                          "frequency": 287.8705471850103,
                          "midi": 62,
                          "cents_from_base": 465.5,
                          "prime_sources": [
                            21433,
                            42863,
                            85733,
                            85751,
                            85781
                          ]
                        },
                        {
                          "log_position": 0.5134166666666666,
                          "frequency": 314.03387470162096,
                          "midi": 63,
                          "cents_from_base": 616.0999999999999,
                          "prime_sources": [
                            46769,
                            46771,
                            93523,
                            93529,
                            93553,
                            93557,
                            93559,
                            93563
                          ]
                        },
                        {
                          "log_position": 0.560375,
                          "frequency": 324.42354431975815,
                          "midi": 64,
                          "cents_from_base": 672.4499999999999,
                          "prime_sources": [
                            24169,
                            48311,
                            48313,
                            48337,
                            96643,
                            96661,
                            96667,
                            96671
                          ]
                        },
                        {
                          "log_position": 0.6490833333333333,
                          "frequency": 344.9977270679486,
                          "midi": 65,
                          "cents_from_base": 778.9,
                          "prime_sources": [
                            25693,
                            51383,
                            102761,
                            102763,
                            102769,
                            102793,
                            102797
                          ]
                        },
                        {
                          "log_position": 0.7498333333333334,
                          "frequency": 369.95168174867587,
                          "midi": 66,
                          "cents_from_base": 899.8000000000001,
                          "prime_sources": [
                            27551,
                            55103,
                            55109,
                            55117,
                            110183,
                            110221,
                            110233,
                            110237
                          ]
                        },
                        {
                          "log_position": 0.7719583333333333,
                          "frequency": 375.66894443090075,
                          "midi": 66,
                          "cents_from_base": 926.3499999999999,
                          "prime_sources": [
                            27983,
                            55949,
                            55967,
                            111871,
                            111893,
                            111913,
                            111919
                          ]
                        },
                        {
                          "log_position": 0.8587916666666666,
                          "frequency": 398.9741264473833,
                          "midi": 67,
                          "cents_from_base": 1030.55,
                          "prime_sources": [
                            29717,
                            59407,
                            59417,
                            59419,
                            59441,
                            59443,
                            118819,
                            118831,
                            118843,
                            118861,
                            118873,
                            118891
                          ]
                        },
                        {
                          "log_position": 0.98725,
                          "frequency": 436.12857661178026,
                          "midi": 69,
                          "cents_from_base": 1184.7,
                          "prime_sources": [
                            32479,
                            64937,
                            64951,
                            64969
                          ]
                        }
                      ]
                    }
                    ```
            
                    `log_prime_scale_3_valley.json`
                    ```json
                    {
                      "name": "log_prime_scale_3_valley",
                      "base_frequency": 220.0,
                      "notes": [
                        {
                          "log_position": 0.0,
                          "frequency": 220.0,
                          "midi": 57,
                          "cents_from_base": 0.0,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.1804,
                          "frequency": 249.3035668094442,
                          "midi": 59,
                          "cents_from_base": 216.48000000000002,
                          "prime_sources": [
                            1163,
                            4637,
                            4639,
                            4643,
                            4649,
                            4651,
                            4657,
                            9257,
                            9277,
                            9281,
                            9283,
                            9293,
                            9311,
                            9319
                          ]
                        },
                        {
                          "log_position": 0.6138,
                          "frequency": 336.6626147773795,
                          "midi": 64,
                          "cents_from_base": 736.5600000000001,
                          "prime_sources": [
                            1567,
                            1571,
                            3137,
                            6247,
                            6257,
                            6263,
                            6269,
                            6271,
                            6277,
                            6287,
                            12487,
                            12491,
                            12497,
                            12503,
                            12511,
                            12517,
                            12527,
                            12539,
                            12541,
                            12547,
                            12553,
                            12569,
                            12577,
                            12583
                          ]
                        },
                        {
                          "log_position": 0.6698,
                          "frequency": 349.9875309149005,
                          "midi": 65,
                          "cents_from_base": 803.76,
                          "prime_sources": [
                            1627,
                            3251,
                            3253,
                            3257,
                            3259,
                            3271,
                            6491,
                            6521,
                            6529,
                            12979,
                            12983,
                            13001,
                            13003,
                            13007,
                            13009,
                            13033,
                            13037,
                            13043,
                            13049,
                            13063
                          ]
                        },
                        {
                          "log_position": 1.0,
                          "frequency": 440.0,
                          "midi": 69,
                          "cents_from_base": 1200.0,
                          "prime_sources": []
                        }
                      ]
                    }
                    ```
            
                    `log_prime_scale_6_peak.json`
                    ```json
                    {
                      "name": "log_prime_scale_6_peak",
                      "base_frequency": 220.0,
                      "notes": [
                        {
                          "log_position": 0.0,
                          "frequency": 220.0,
                          "midi": 57,
                          "cents_from_base": 0.0,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.0,
                          "frequency": 220.0,
                          "midi": 57,
                          "cents_from_base": 0.0,
                          "prime_sources": [
                            2,
                            4091,
                            4093,
                            4099,
                            8179,
                            8191,
                            8209,
                            16361,
                            16363,
                            16369,
                            16381,
                            16411,
                            16417,
                            32707,
                            32713,
                            32717,
                            32719,
                            32749,
                            32771,
                            32779,
                            32783,
                            32789,
                            32797,
                            32801,
                            32803,
                            32831,
                            32833
                          ]
                        },
                        {
                          "log_position": 0.322,
                          "frequency": 275.013706568746,
                          "midi": 61,
                          "cents_from_base": 386.40000000000003,
                          "prime_sources": [
                            5,
                            641,
                            1279,
                            2557,
                            5113,
                            5119,
                            10223,
                            10243,
                            10247,
                            10253,
                            10259,
                            20441,
                            20443,
                            20477,
                            20479,
                            20483,
                            20507,
                            20509,
                            20521
                          ]
                        },
                        {
                          "log_position": 0.4594,
                          "frequency": 302.493370370937,
                          "midi": 63,
                          "cents_from_base": 551.28,
                          "prime_sources": [
                            11,
                            1409,
                            2819,
                            5623,
                            5639,
                            5641,
                            11243,
                            11251,
                            11257,
                            11261,
                            11273,
                            11279,
                            11287,
                            22481,
                            22483,
                            22501,
                            22511,
                            22531,
                            22541,
                            22543,
                            22549,
                            22567,
                            22571,
                            22573
                          ]
                        },
                        {
                          "log_position": 0.585,
                          "frequency": 330.00857764287997,
                          "midi": 64,
                          "cents_from_base": 702.0,
                          "prime_sources": [
                            3,
                            769,
                            3067,
                            6133,
                            6143,
                            6151,
                            12263,
                            12269,
                            12277,
                            12281,
                            12289,
                            12301,
                            24527,
                            24533,
                            24547,
                            24551,
                            24571,
                            24593,
                            24611,
                            24623
                          ]
                        },
                        {
                          "log_position": 0.8076,
                          "frequency": 385.0654074630357,
                          "midi": 67,
                          "cents_from_base": 969.12,
                          "prime_sources": [
                            7,
                            449,
                            1789,
                            3581,
                            3583,
                            7159,
                            7177,
                            14321,
                            14323,
                            14327,
                            14341,
                            14347,
                            28619,
                            28621,
                            28627,
                            28631,
                            28643,
                            28649,
                            28657,
                            28661,
                            28663,
                            28669,
                            28687,
                            28697,
                            28703,
                            28711,
                            28723,
                            28729
                          ]
                        },
                        {
                          "log_position": 0.9998,
                          "frequency": 439.9390072759019,
                          "midi": 69,
                          "cents_from_base": 1199.76,
                          "prime_sources": [
                            2,
                            4091,
                            4093,
                            4099,
                            8179,
                            8191,
                            16349,
                            16361,
                            16363,
                            16369,
                            16381,
                            16411,
                            32707,
                            32713,
                            32717,
                            32719,
                            32749,
                            32771,
                            32779,
                            32783,
                            32789,
                            32797,
                            32801,
                            32803,
                            32831
                          ]
                        },
                        {
                          "log_position": 1.0,
                          "frequency": 440.0,
                          "midi": 69,
                          "cents_from_base": 1200.0,
                          "prime_sources": []
                        }
                      ]
                    }
                    ```
            
                    `log_prime_scale_6_valley.json`
                    ```json
                    {
                      "name": "log_prime_scale_6_valley",
                      "base_frequency": 220.0,
                      "notes": [
                        {
                          "log_position": 0.0,
                          "frequency": 220.0,
                          "midi": 57,
                          "cents_from_base": 0.0,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.075375,
                          "frequency": 231.79967181348457,
                          "midi": 58,
                          "cents_from_base": 90.45,
                          "prime_sources": [
                            8623,
                            8627,
                            8629,
                            8641,
                            17239,
                            17257,
                            34483,
                            34487,
                            34499,
                            34501,
                            34511,
                            34513,
                            34519,
                            34537,
                            34543,
                            34549
                          ]
                        },
                        {
                          "log_position": 0.176875,
                          "frequency": 248.6951760388849,
                          "midi": 59,
                          "cents_from_base": 212.25,
                          "prime_sources": [
                            9257,
                            18503,
                            18517,
                            18521,
                            18523,
                            18539,
                            18541,
                            36997,
                            37003,
                            37013,
                            37019,
                            37021,
                            37039,
                            37049,
                            37057,
                            37061,
                            37087
                          ]
                        },
                        {
                          "log_position": 0.43675,
                          "frequency": 297.78137534016145,
                          "midi": 62,
                          "cents_from_base": 524.1,
                          "prime_sources": [
                            11083,
                            11087,
                            11093,
                            22147,
                            22153,
                            22157,
                            22159,
                            22171,
                            22189,
                            22193,
                            44293,
                            44351,
                            44357,
                            44371,
                            44381,
                            44383,
                            44389
                          ]
                        },
                        {
                          "log_position": 0.610625,
                          "frequency": 335.9225217964596,
                          "midi": 64,
                          "cents_from_base": 732.75,
                          "prime_sources": [
                            6247,
                            6257,
                            12497,
                            12503,
                            12511,
                            12517,
                            24989,
                            25013,
                            25031,
                            25033,
                            25037,
                            49991,
                            49993,
                            49999,
                            50021,
                            50023,
                            50033,
                            50047,
                            50051,
                            50053,
                            50069,
                            50077,
                            50087,
                            50093,
                            50101
                          ]
                        },
                        {
                          "log_position": 0.6735,
                          "frequency": 350.88627652385884,
                          "midi": 65,
                          "cents_from_base": 808.1999999999999,
                          "prime_sources": [
                            6529,
                            13049,
                            13063,
                            26099,
                            26107,
                            26111,
                            26113,
                            26119,
                            26141,
                            26153,
                            26161,
                            52201,
                            52223,
                            52237,
                            52249,
                            52253,
                            52259,
                            52267,
                            52289,
                            52291,
                            52301,
                            52313,
                            52321
                          ]
                        },
                        {
                          "log_position": 0.958625,
                          "frequency": 427.56048438765623,
                          "midi": 69,
                          "cents_from_base": 1150.35,
                          "prime_sources": [
                            7951,
                            7963,
                            15901,
                            15907,
                            15913,
                            15919,
                            15923,
                            15937,
                            31799,
                            31817,
                            31847,
                            31849,
                            31859,
                            31873,
                            31883
                          ]
                        },
                        {
                          "log_position": 1.0,
                          "frequency": 440.0,
                          "midi": 69,
                          "cents_from_base": 1200.0,
                          "prime_sources": []
                        }
                      ]
                    }
                    ```
            
                    `manifest.json`
                    ```json
                    {
                      "scales": [
                        "gap_scout_match_5_notes.json",
                        "log_prime_scale_3_valley.json",
                        "log_prime_scale_6_valley.json",
                        "log_prime_scale_6_peak.json",
                        "log_prime_scale_13_valley.json",
                        "pure_prime_scale_128_primes.json",
                        "sample_scale.json",
                        "terrain_scale_8_valley.json"
                      ]
                    }
                    ```
            
                    `pure_prime_scale_128_primes.json`
                    ```json
                    {
                      "name": "pure_prime_scale_128_primes",
                      "base_frequency": 220.0,
                      "notes": [
                        {
                          "log_position": 0.0,
                          "frequency": 220.0,
                          "midi": 57,
                          "cents_from_base": 0.0,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.0,
                          "frequency": 220.0,
                          "midi": 57,
                          "cents_from_base": 0.0,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.5849625007211562,
                          "frequency": 330.0,
                          "midi": 64,
                          "cents_from_base": 701.9550008653874,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.32192809488736235,
                          "frequency": 275.0,
                          "midi": 61,
                          "cents_from_base": 386.3137138648348,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.8073549220576041,
                          "frequency": 385.0,
                          "midi": 67,
                          "cents_from_base": 968.8259064691249,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.45943161863729726,
                          "frequency": 302.5,
                          "midi": 63,
                          "cents_from_base": 551.3179423647567,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.7004397181410922,
                          "frequency": 357.5,
                          "midi": 65,
                          "cents_from_base": 840.5276617693106,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.0874628412503394,
                          "frequency": 233.75,
                          "midi": 58,
                          "cents_from_base": 104.95540950040728,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.2479275134435855,
                          "frequency": 261.25,
                          "midi": 60,
                          "cents_from_base": 297.5130161323026,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.5235619560570128,
                          "frequency": 316.25,
                          "midi": 63,
                          "cents_from_base": 628.2743472684155,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.8579809951275721,
                          "frequency": 398.75,
                          "midi": 67,
                          "cents_from_base": 1029.5771941530866,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.9541963103868752,
                          "frequency": 426.25,
                          "midi": 68,
                          "cents_from_base": 1145.0355724642502,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.20945336562894978,
                          "frequency": 254.375,
                          "midi": 60,
                          "cents_from_base": 251.34403875473973,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.3575520046180837,
                          "frequency": 281.875,
                          "midi": 61,
                          "cents_from_base": 429.0624055417004,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.42626475470209796,
                          "frequency": 295.625,
                          "midi": 62,
                          "cents_from_base": 511.51770564251757,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.5545888516776374,
                          "frequency": 323.125,
                          "midi": 64,
                          "cents_from_base": 665.5066220131648,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.7279204545631992,
                          "frequency": 364.375,
                          "midi": 66,
                          "cents_from_base": 873.504545475839,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.8826430493618412,
                          "frequency": 405.625,
                          "midi": 68,
                          "cents_from_base": 1059.1716592342095,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.9307373375628862,
                          "frequency": 419.375,
                          "midi": 68,
                          "cents_from_base": 1116.8848050754634,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.06608919045777244,
                          "frequency": 230.3125,
                          "midi": 58,
                          "cents_from_base": 79.30702854932693,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.14974711950468206,
                          "frequency": 244.0625,
                          "midi": 59,
                          "cents_from_base": 179.69654340561846,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.18982455888001723,
                          "frequency": 250.9375,
                          "midi": 59,
                          "cents_from_base": 227.78947065602068,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.30378074817710293,
                          "frequency": 271.5625,
                          "midi": 61,
                          "cents_from_base": 364.53689781252353,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.37503943134692475,
                          "frequency": 285.3125,
                          "midi": 62,
                          "cents_from_base": 450.04731761630967,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.47573343096639775,
                          "frequency": 305.9375,
                          "midi": 63,
                          "cents_from_base": 570.8801171596773,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.5999128421871277,
                          "frequency": 333.4375,
                          "midi": 64,
                          "cents_from_base": 719.8954106245533,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.6582114827517948,
                          "frequency": 347.1875,
                          "midi": 65,
                          "cents_from_base": 789.8537793021537,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.6865005271832184,
                          "frequency": 354.0625,
                          "midi": 65,
                          "cents_from_base": 823.8006326198621,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.7414669864011469,
                          "frequency": 367.8125,
                          "midi": 66,
                          "cents_from_base": 889.7603836813763,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.7681843247769263,
                          "frequency": 374.6875,
                          "midi": 66,
                          "cents_from_base": 921.8211897323116,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.8201789624151877,
                          "frequency": 388.4375,
                          "midi": 67,
                          "cents_from_base": 984.2147548982252,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.9886846867721658,
                          "frequency": 436.5625,
                          "midi": 69,
                          "cents_from_base": 1186.421624126599,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.03342300153745028,
                          "frequency": 225.15625,
                          "midi": 57,
                          "cents_from_base": 40.10760184494033,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.09803208296052672,
                          "frequency": 235.46875,
                          "midi": 58,
                          "cents_from_base": 117.63849955263207,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.11894107272350743,
                          "frequency": 238.90625,
                          "midi": 58,
                          "cents_from_base": 142.7292872682089,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.21916852046216156,
                          "frequency": 256.09375,
                          "midi": 60,
                          "cents_from_base": 263.00222455459385,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.2384047393250789,
                          "frequency": 259.53125,
                          "midi": 60,
                          "cents_from_base": 286.0856871900947,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.294620748891627,
                          "frequency": 269.84375,
                          "midi": 61,
                          "cents_from_base": 353.5448986699524,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.34872815423107756,
                          "frequency": 280.15625,
                          "midi": 61,
                          "cents_from_base": 418.4737850772931,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.38370429247405224,
                          "frequency": 287.03125,
                          "midi": 62,
                          "cents_from_base": 460.4451509688627,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.43462822763672465,
                          "frequency": 297.34375,
                          "midi": 62,
                          "cents_from_base": 521.5538731640696,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.4838157772642564,
                          "frequency": 307.65625,
                          "midi": 63,
                          "cents_from_base": 580.5789327171077,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.4998458870832054,
                          "frequency": 311.09375,
                          "midi": 63,
                          "cents_from_base": 599.8150644998465,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.5774288280357487,
                          "frequency": 328.28125,
                          "midi": 64,
                          "cents_from_base": 692.9145936428985,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.5924570372680804,
                          "frequency": 331.71875,
                          "midi": 64,
                          "cents_from_base": 710.9484447216965,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.6220518194563762,
                          "frequency": 338.59375,
                          "midi": 64,
                          "cents_from_base": 746.4621833476515,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.6366246205436489,
                          "frequency": 342.03125,
                          "midi": 65,
                          "cents_from_base": 763.9495446523787,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.7210991887071851,
                          "frequency": 362.65625,
                          "midi": 66,
                          "cents_from_base": 865.3190264486221,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.8008998999203047,
                          "frequency": 383.28125,
                          "midi": 67,
                          "cents_from_base": 961.0798799043657,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.826548487290915,
                          "frequency": 390.15625,
                          "midi": 67,
                          "cents_from_base": 991.858184749098,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.839203788096944,
                          "frequency": 393.59375,
                          "midi": 67,
                          "cents_from_base": 1007.0445457163328,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.8641861446542802,
                          "frequency": 400.46875,
                          "midi": 67,
                          "cents_from_base": 1037.0233735851364,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.9008668079807486,
                          "frequency": 410.78125,
                          "midi": 68,
                          "cents_from_base": 1081.0401695768983,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.9128893362299616,
                          "frequency": 414.21875,
                          "midi": 68,
                          "cents_from_base": 1095.467203475954,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.971543553950772,
                          "frequency": 431.40625,
                          "midi": 69,
                          "cents_from_base": 1165.8522647409263,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.005624549193878107,
                          "frequency": 220.859375,
                          "midi": 57,
                          "cents_from_base": 6.749459032653728,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.03891898929230235,
                          "frequency": 226.015625,
                          "midi": 57,
                          "cents_from_base": 46.70278715076282,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.07146236255662415,
                          "frequency": 231.171875,
                          "midi": 58,
                          "cents_from_base": 85.75483506794897,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.08214904135387156,
                          "frequency": 232.890625,
                          "midi": 58,
                          "cents_from_base": 98.57884962464587,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.11374216604918833,
                          "frequency": 238.046875,
                          "midi": 58,
                          "cents_from_base": 136.490599259026,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.1344263202209261,
                          "frequency": 241.484375,
                          "midi": 59,
                          "cents_from_base": 161.31158426511132,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.14465824283188233,
                          "frequency": 243.203125,
                          "midi": 59,
                          "cents_from_base": 173.5898913982588,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.19475685442224788,
                          "frequency": 251.796875,
                          "midi": 59,
                          "cents_from_base": 233.70822530669747,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.2620948453701794,
                          "frequency": 263.828125,
                          "midi": 60,
                          "cents_from_base": 314.5138144442153,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.28077077013060253,
                          "frequency": 267.265625,
                          "midi": 60,
                          "cents_from_base": 336.924924156723,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.2900188469326183,
                          "frequency": 268.984375,
                          "midi": 60,
                          "cents_from_base": 348.022616319142,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.3083390301394073,
                          "frequency": 272.421875,
                          "midi": 61,
                          "cents_from_base": 370.0068361672887,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.3706874068072177,
                          "frequency": 284.453125,
                          "midi": 61,
                          "cents_from_base": 444.82488816866123,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.3966047811818585,
                          "frequency": 289.609375,
                          "midi": 62,
                          "cents_from_base": 475.9257374182302,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.4387918525782609,
                          "frequency": 298.203125,
                          "midi": 62,
                          "cents_from_base": 526.5502230939131,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.44708322620965224,
                          "frequency": 299.921875,
                          "midi": 62,
                          "cents_from_base": 536.4998714515826,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.4635243732711803,
                          "frequency": 303.359375,
                          "midi": 63,
                          "cents_from_base": 556.2292479254163,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.48784003382305136,
                          "frequency": 308.515625,
                          "midi": 63,
                          "cents_from_base": 585.4080405876616,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.5196362528432128,
                          "frequency": 315.390625,
                          "midi": 63,
                          "cents_from_base": 623.5635034118553,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.5430318202552378,
                          "frequency": 320.546875,
                          "midi": 64,
                          "cents_from_base": 651.6381843062853,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.5660540381710917,
                          "frequency": 325.703125,
                          "midi": 64,
                          "cents_from_base": 679.26484580531,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.581200581924957,
                          "frequency": 329.140625,
                          "midi": 64,
                          "cents_from_base": 697.4406983099484,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.6036263449861919,
                          "frequency": 334.296875,
                          "midi": 64,
                          "cents_from_base": 724.3516139834303,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.6329951971429578,
                          "frequency": 341.171875,
                          "midi": 65,
                          "cents_from_base": 759.5942365715493,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.6474584264549202,
                          "frequency": 344.609375,
                          "midi": 65,
                          "cents_from_base": 776.9501117459043,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.6759570329417488,
                          "frequency": 351.484375,
                          "midi": 65,
                          "cents_from_base": 811.1484395300986,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.7108064336993516,
                          "frequency": 360.078125,
                          "midi": 66,
                          "cents_from_base": 852.9677204392219,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.7176764230663961,
                          "frequency": 361.796875,
                          "midi": 66,
                          "cents_from_base": 861.2117076796753,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.7515440590890982,
                          "frequency": 370.390625,
                          "midi": 66,
                          "cents_from_base": 901.8528709069178,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.7582232147267249,
                          "frequency": 372.109375,
                          "midi": 66,
                          "cents_from_base": 909.8678576720699,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.7780771295353582,
                          "frequency": 377.265625,
                          "midi": 66,
                          "cents_from_base": 933.6925554424299,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.7911628885550183,
                          "frequency": 380.703125,
                          "midi": 66,
                          "cents_from_base": 949.3954662660219,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.8105716347411469,
                          "frequency": 385.859375,
                          "midi": 67,
                          "cents_from_base": 972.6859616893763,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.8360503550580697,
                          "frequency": 392.734375,
                          "midi": 67,
                          "cents_from_base": 1003.2604260696836,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.848622940429338,
                          "frequency": 396.171875,
                          "midi": 67,
                          "cents_from_base": 1018.3475285152056,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.8548683832602364,
                          "frequency": 397.890625,
                          "midi": 67,
                          "cents_from_base": 1025.8420599122837,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.867278739709662,
                          "frequency": 401.328125,
                          "midi": 67,
                          "cents_from_base": 1040.7344876515945,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.9038818457361802,
                          "frequency": 411.640625,
                          "midi": 68,
                          "cents_from_base": 1084.6582148834163,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.9277779620823422,
                          "frequency": 418.515625,
                          "midi": 68,
                          "cents_from_base": 1113.3335544988106,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.939579214314693,
                          "frequency": 421.953125,
                          "midi": 68,
                          "cents_from_base": 1127.4950571776317,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.9628960053372605,
                          "frequency": 428.828125,
                          "midi": 69,
                          "cents_from_base": 1155.4752064047127,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.9744145898055271,
                          "frequency": 432.265625,
                          "midi": 69,
                          "cents_from_base": 1169.2975077666324,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.9915218460756953,
                          "frequency": 437.421875,
                          "midi": 69,
                          "cents_from_base": 1189.8262152908344,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.025139562278508228,
                          "frequency": 223.8671875,
                          "midi": 57,
                          "cents_from_base": 30.167474734209872,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.030667136246941375,
                          "frequency": 224.7265625,
                          "midi": 57,
                          "cents_from_base": 36.80056349632965,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.07948478382681526,
                          "frequency": 232.4609375,
                          "midi": 58,
                          "cents_from_base": 95.3817405921783,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.09539702279255656,
                          "frequency": 235.0390625,
                          "midi": 58,
                          "cents_from_base": 114.47642735106787,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.12153351734003176,
                          "frequency": 239.3359375,
                          "midi": 58,
                          "cents_from_base": 145.8402208080381,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.13699111208022957,
                          "frequency": 241.9140625,
                          "midi": 59,
                          "cents_from_base": 164.3893344962755,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.15228484230658193,
                          "frequency": 244.4921875,
                          "midi": 59,
                          "cents_from_base": 182.74181076789833,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.15734693536284278,
                          "frequency": 245.3515625,
                          "midi": 59,
                          "cents_from_base": 188.81632243541134,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.17242750864548248,
                          "frequency": 247.9296875,
                          "midi": 59,
                          "cents_from_base": 206.913010374579,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.1972166931100522,
                          "frequency": 252.2265625,
                          "midi": 59,
                          "cents_from_base": 236.66003173206263,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.21188829454600366,
                          "frequency": 254.8046875,
                          "midi": 60,
                          "cents_from_base": 254.2659534552044,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.22641219278878566,
                          "frequency": 257.3828125,
                          "midi": 60,
                          "cents_from_base": 271.6946313465428,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.23122118071118544,
                          "frequency": 258.2421875,
                          "midi": 60,
                          "cents_from_base": 277.46541685342254,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.24555270625568207,
                          "frequency": 260.8203125,
                          "midi": 60,
                          "cents_from_base": 294.6632475068185,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.2597432636907815,
                          "frequency": 263.3984375,
                          "midi": 60,
                          "cents_from_base": 311.6919164289378,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.2691266791494179,
                          "frequency": 265.1171875,
                          "midi": 60,
                          "cents_from_base": 322.9520149793015,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.27379559921426466,
                          "frequency": 265.9765625,
                          "midi": 60,
                          "cents_from_base": 328.5547190571176,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.301496194982549,
                          "frequency": 271.1328125,
                          "midi": 61,
                          "cents_from_base": 361.79543397905877,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.324180546618741,
                          "frequency": 275.4296875,
                          "midi": 61,
                          "cents_from_base": 389.0166559424892,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.32867492732794734,
                          "frequency": 276.2890625,
                          "midi": 61,
                          "cents_from_base": 394.4099127935368,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.3376219019925075,
                          "frequency": 278.0078125,
                          "midi": 61,
                          "cents_from_base": 405.14628239100904,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.3509391815464308,
                          "frequency": 280.5859375,
                          "midi": 61,
                          "cents_from_base": 421.12701785571693,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.36413465500805176,
                          "frequency": 283.1640625,
                          "midi": 61,
                          "cents_from_base": 436.9615860096621,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.3685064615076917,
                          "frequency": 284.0234375,
                          "midi": 61,
                          "cents_from_base": 442.20775380923,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.3944626946103171,
                          "frequency": 289.1796875,
                          "midi": 62,
                          "cents_from_base": 473.3552335323805,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.40301202357499677,
                          "frequency": 290.8984375,
                          "midi": 62,
                          "cents_from_base": 483.6144282899961,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.41574176829009046,
                          "frequency": 293.4765625,
                          "midi": 62,
                          "cents_from_base": 498.8901219481086,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.4325419003882585,
                          "frequency": 296.9140625,
                          "midi": 62,
                          "cents_from_base": 519.0502804659102,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.4532706340106232,
                          "frequency": 301.2109375,
                          "midi": 62,
                          "cents_from_base": 543.9247608127478,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.4696418172395161,
                          "frequency": 304.6484375,
                          "midi": 63,
                          "cents_from_base": 563.5701806874193,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.4898479604392978,
                          "frequency": 308.9453125,
                          "midi": 63,
                          "cents_from_base": 587.8175525271573,
                          "prime_sources": []
                        },
                        {
                          "log_position": 1.0,
                          "frequency": 440.0,
                          "midi": 69,
                          "cents_from_base": 1200.0,
                          "prime_sources": []
                        }
                      ]
                    }
                    ```
            
                    `sample_scale.json`
                    ```json
                    {
                      "name": "sample_scale",
                      "base_frequency": 220.0,
                      "notes": [
                        {
                          "frequency": 220.0,
                          "cents_from_base": 0.0,
                          "midi": 57,
                          "log_position": 0.0,
                          "prime_sources": []
                        },
                        {
                          "frequency": 246.94,
                          "cents_from_base": 200.0,
                          "midi": 59,
                          "log_position": 0.1667,
                          "prime_sources": [
                            3
                          ]
                        },
                        {
                          "frequency": 261.63,
                          "cents_from_base": 300.0,
                          "midi": 60,
                          "log_position": 0.25,
                          "prime_sources": [
                            5
                          ]
                        },
                        {
                          "frequency": 293.66,
                          "cents_from_base": 500.0,
                          "midi": 62,
                          "log_position": 0.4167,
                          "prime_sources": [
                            7
                          ]
                        },
                        {
                          "frequency": 329.63,
                          "cents_from_base": 700.0,
                          "midi": 64,
                          "log_position": 0.5833,
                          "prime_sources": [
                            11
                          ]
                        },
                        {
                          "frequency": 392.0,
                          "cents_from_base": 900.0,
                          "midi": 67,
                          "log_position": 0.75,
                          "prime_sources": [
                            13
                          ]
                        },
                        {
                          "frequency": 440.0,
                          "cents_from_base": 1200.0,
                          "midi": 69,
                          "log_position": 1.0,
                          "prime_sources": []
                        }
                      ]
                    }
                    ```
            
                    `terrain_scale_8_valley.json`
                    ```json
                    {
                      "name": "terrain_scale_8_valley",
                      "base_frequency": 220.0,
                      "notes": [
                        {
                          "log_position": 0.0,
                          "frequency": 220.0,
                          "midi": 57,
                          "cents_from_base": 0.0,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.07575,
                          "frequency": 231.85993137814998,
                          "midi": 58,
                          "cents_from_base": 90.89999999999999,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.178,
                          "frequency": 248.88918182609805,
                          "midi": 59,
                          "cents_from_base": 213.6,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.2845,
                          "frequency": 267.9573749645833,
                          "midi": 60,
                          "cents_from_base": 341.4,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.495,
                          "frequency": 310.0505661312443,
                          "midi": 63,
                          "cents_from_base": 594.0,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.61025,
                          "frequency": 335.8352167377353,
                          "midi": 64,
                          "cents_from_base": 732.3,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.672,
                          "frequency": 350.5216423656564,
                          "midi": 65,
                          "cents_from_base": 806.4000000000001,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.763,
                          "frequency": 373.3434767505944,
                          "midi": 66,
                          "cents_from_base": 915.6,
                          "prime_sources": []
                        },
                        {
                          "log_position": 0.95775,
                          "frequency": 427.3012459589087,
                          "midi": 68,
                          "cents_from_base": 1149.3,
                          "prime_sources": []
                        },
                        {
                          "log_position": 1.0,
                          "frequency": 440.0,
                          "midi": 69,
                          "cents_from_base": 1200.0,
                          "prime_sources": []
                        }
                      ]
                    }
                    ```
            ```

            `output/gap_scout_match_5_notes.json`
            ```json
            {
              "name": "gap_scout_match_5_notes",
              "base_frequency": 220.0,
              "notes": [
                {
                  "log_position": 0.0,
                  "frequency": 220.0,
                  "midi": 57,
                  "cents_from_base": 0.0,
                  "prime_sources": []
                },
                {
                  "log_position": 0.07480798051337051,
                  "frequency": 231.70858596251097,
                  "midi": 58,
                  "cents_from_base": 89.76957661604462,
                  "prime_sources": []
                },
                {
                  "log_position": 0.6107910531958953,
                  "frequency": 335.9611884703146,
                  "midi": 64,
                  "cents_from_base": 732.9492638350744,
                  "prime_sources": []
                },
                {
                  "log_position": 0.6728648404106712,
                  "frequency": 350.73182965589353,
                  "midi": 65,
                  "cents_from_base": 807.4378084928054,
                  "prime_sources": []
                },
                {
                  "log_position": 0.7630023064687417,
                  "frequency": 373.34407362361526,
                  "midi": 66,
                  "cents_from_base": 915.60276776249,
                  "prime_sources": []
                },
                {
                  "log_position": 0.9068881985485664,
                  "frequency": 412.4993146254886,
                  "midi": 68,
                  "cents_from_base": 1088.2658382582797,
                  "prime_sources": []
                },
                {
                  "log_position": 1.0,
                  "frequency": 440.0,
                  "midi": 69,
                  "cents_from_base": 1200.0,
                  "prime_sources": []
                }
              ]
            }
            ```

            `output/log_prime_scale_13_valley.json`
            ```json
            {
              "name": "log_prime_scale_13_valley",
              "base_frequency": 220.0,
              "notes": [
                {
                  "log_position": 0.029291666666666667,
                  "frequency": 224.5124096554435,
                  "midi": 57,
                  "cents_from_base": 35.15,
                  "prime_sources": [
                    66863,
                    66877,
                    66883,
                    66889
                  ]
                },
                {
                  "log_position": 0.12095833333333333,
                  "frequency": 239.24053635066036,
                  "midi": 58,
                  "cents_from_base": 145.15,
                  "prime_sources": [
                    71249,
                    71257,
                    71261,
                    71263,
                    71287
                  ]
                },
                {
                  "log_position": 0.17775,
                  "frequency": 248.84605635407974,
                  "midi": 59,
                  "cents_from_base": 213.29999999999998,
                  "prime_sources": [
                    37057,
                    37061,
                    74131,
                    74143,
                    74149
                  ]
                },
                {
                  "log_position": 0.25783333333333336,
                  "frequency": 263.0499648117823,
                  "midi": 60,
                  "cents_from_base": 309.40000000000003,
                  "prime_sources": [
                    39181,
                    39191,
                    78341,
                    78347,
                    78367
                  ]
                },
                {
                  "log_position": 0.363375,
                  "frequency": 283.0150009385238,
                  "midi": 61,
                  "cents_from_base": 436.05,
                  "prime_sources": [
                    42157,
                    84299,
                    84307,
                    84313,
                    84317,
                    84319
                  ]
                },
                {
                  "log_position": 0.3879166666666667,
                  "frequency": 287.8705471850103,
                  "midi": 62,
                  "cents_from_base": 465.5,
                  "prime_sources": [
                    21433,
                    42863,
                    85733,
                    85751,
                    85781
                  ]
                },
                {
                  "log_position": 0.5134166666666666,
                  "frequency": 314.03387470162096,
                  "midi": 63,
                  "cents_from_base": 616.0999999999999,
                  "prime_sources": [
                    46769,
                    46771,
                    93523,
                    93529,
                    93553,
                    93557,
                    93559,
                    93563
                  ]
                },
                {
                  "log_position": 0.560375,
                  "frequency": 324.42354431975815,
                  "midi": 64,
                  "cents_from_base": 672.4499999999999,
                  "prime_sources": [
                    24169,
                    48311,
                    48313,
                    48337,
                    96643,
                    96661,
                    96667,
                    96671
                  ]
                },
                {
                  "log_position": 0.6490833333333333,
                  "frequency": 344.9977270679486,
                  "midi": 65,
                  "cents_from_base": 778.9,
                  "prime_sources": [
                    25693,
                    51383,
                    102761,
                    102763,
                    102769,
                    102793,
                    102797
                  ]
                },
                {
                  "log_position": 0.7498333333333334,
                  "frequency": 369.95168174867587,
                  "midi": 66,
                  "cents_from_base": 899.8000000000001,
                  "prime_sources": [
                    27551,
                    55103,
                    55109,
                    55117,
                    110183,
                    110221,
                    110233,
                    110237
                  ]
                },
                {
                  "log_position": 0.7719583333333333,
                  "frequency": 375.66894443090075,
                  "midi": 66,
                  "cents_from_base": 926.3499999999999,
                  "prime_sources": [
                    27983,
                    55949,
                    55967,
                    111871,
                    111893,
                    111913,
                    111919
                  ]
                },
                {
                  "log_position": 0.8587916666666666,
                  "frequency": 398.9741264473833,
                  "midi": 67,
                  "cents_from_base": 1030.55,
                  "prime_sources": [
                    29717,
                    59407,
                    59417,
                    59419,
                    59441,
                    59443,
                    118819,
                    118831,
                    118843,
                    118861,
                    118873,
                    118891
                  ]
                },
                {
                  "log_position": 0.98725,
                  "frequency": 436.12857661178026,
                  "midi": 69,
                  "cents_from_base": 1184.7,
                  "prime_sources": [
                    32479,
                    64937,
                    64951,
                    64969
                  ]
                }
              ]
            }
            ```

            `output/log_prime_scale_3_valley.json`
            ```json
            {
              "name": "log_prime_scale_3_valley",
              "base_frequency": 220.0,
              "notes": [
                {
                  "log_position": 0.0,
                  "frequency": 220.0,
                  "midi": 57,
                  "cents_from_base": 0.0,
                  "prime_sources": []
                },
                {
                  "log_position": 0.1804,
                  "frequency": 249.3035668094442,
                  "midi": 59,
                  "cents_from_base": 216.48000000000002,
                  "prime_sources": [
                    1163,
                    4637,
                    4639,
                    4643,
                    4649,
                    4651,
                    4657,
                    9257,
                    9277,
                    9281,
                    9283,
                    9293,
                    9311,
                    9319
                  ]
                },
                {
                  "log_position": 0.6138,
                  "frequency": 336.6626147773795,
                  "midi": 64,
                  "cents_from_base": 736.5600000000001,
                  "prime_sources": [
                    1567,
                    1571,
                    3137,
                    6247,
                    6257,
                    6263,
                    6269,
                    6271,
                    6277,
                    6287,
                    12487,
                    12491,
                    12497,
                    12503,
                    12511,
                    12517,
                    12527,
                    12539,
                    12541,
                    12547,
                    12553,
                    12569,
                    12577,
                    12583
                  ]
                },
                {
                  "log_position": 0.6698,
                  "frequency": 349.9875309149005,
                  "midi": 65,
                  "cents_from_base": 803.76,
                  "prime_sources": [
                    1627,
                    3251,
                    3253,
                    3257,
                    3259,
                    3271,
                    6491,
                    6521,
                    6529,
                    12979,
                    12983,
                    13001,
                    13003,
                    13007,
                    13009,
                    13033,
                    13037,
                    13043,
                    13049,
                    13063
                  ]
                },
                {
                  "log_position": 1.0,
                  "frequency": 440.0,
                  "midi": 69,
                  "cents_from_base": 1200.0,
                  "prime_sources": []
                }
              ]
            }
            ```

            `output/log_prime_scale_6_peak.json`
            ```json
            {
              "name": "log_prime_scale_6_peak",
              "base_frequency": 220.0,
              "notes": [
                {
                  "log_position": 0.0,
                  "frequency": 220.0,
                  "midi": 57,
                  "cents_from_base": 0.0,
                  "prime_sources": []
                },
                {
                  "log_position": 0.0,
                  "frequency": 220.0,
                  "midi": 57,
                  "cents_from_base": 0.0,
                  "prime_sources": [
                    2,
                    4091,
                    4093,
                    4099,
                    8179,
                    8191,
                    8209,
                    16361,
                    16363,
                    16369,
                    16381,
                    16411,
                    16417,
                    32707,
                    32713,
                    32717,
                    32719,
                    32749,
                    32771,
                    32779,
                    32783,
                    32789,
                    32797,
                    32801,
                    32803,
                    32831,
                    32833
                  ]
                },
                {
                  "log_position": 0.322,
                  "frequency": 275.013706568746,
                  "midi": 61,
                  "cents_from_base": 386.40000000000003,
                  "prime_sources": [
                    5,
                    641,
                    1279,
                    2557,
                    5113,
                    5119,
                    10223,
                    10243,
                    10247,
                    10253,
                    10259,
                    20441,
                    20443,
                    20477,
                    20479,
                    20483,
                    20507,
                    20509,
                    20521
                  ]
                },
                {
                  "log_position": 0.4594,
                  "frequency": 302.493370370937,
                  "midi": 63,
                  "cents_from_base": 551.28,
                  "prime_sources": [
                    11,
                    1409,
                    2819,
                    5623,
                    5639,
                    5641,
                    11243,
                    11251,
                    11257,
                    11261,
                    11273,
                    11279,
                    11287,
                    22481,
                    22483,
                    22501,
                    22511,
                    22531,
                    22541,
                    22543,
                    22549,
                    22567,
                    22571,
                    22573
                  ]
                },
                {
                  "log_position": 0.585,
                  "frequency": 330.00857764287997,
                  "midi": 64,
                  "cents_from_base": 702.0,
                  "prime_sources": [
                    3,
                    769,
                    3067,
                    6133,
                    6143,
                    6151,
                    12263,
                    12269,
                    12277,
                    12281,
                    12289,
                    12301,
                    24527,
                    24533,
                    24547,
                    24551,
                    24571,
                    24593,
                    24611,
                    24623
                  ]
                },
                {
                  "log_position": 0.8076,
                  "frequency": 385.0654074630357,
                  "midi": 67,
                  "cents_from_base": 969.12,
                  "prime_sources": [
                    7,
                    449,
                    1789,
                    3581,
                    3583,
                    7159,
                    7177,
                    14321,
                    14323,
                    14327,
                    14341,
                    14347,
                    28619,
                    28621,
                    28627,
                    28631,
                    28643,
                    28649,
                    28657,
                    28661,
                    28663,
                    28669,
                    28687,
                    28697,
                    28703,
                    28711,
                    28723,
                    28729
                  ]
                },
                {
                  "log_position": 0.9998,
                  "frequency": 439.9390072759019,
                  "midi": 69,
                  "cents_from_base": 1199.76,
                  "prime_sources": [
                    2,
                    4091,
                    4093,
                    4099,
                    8179,
                    8191,
                    16349,
                    16361,
                    16363,
                    16369,
                    16381,
                    16411,
                    32707,
                    32713,
                    32717,
                    32719,
                    32749,
                    32771,
                    32779,
                    32783,
                    32789,
                    32797,
                    32801,
                    32803,
                    32831
                  ]
                },
                {
                  "log_position": 1.0,
                  "frequency": 440.0,
                  "midi": 69,
                  "cents_from_base": 1200.0,
                  "prime_sources": []
                }
              ]
            }
            ```

            `output/log_prime_scale_6_valley.json`
            ```json
            {
              "name": "log_prime_scale_6_valley",
              "base_frequency": 220.0,
              "notes": [
                {
                  "log_position": 0.0,
                  "frequency": 220.0,
                  "midi": 57,
                  "cents_from_base": 0.0,
                  "prime_sources": []
                },
                {
                  "log_position": 0.075375,
                  "frequency": 231.79967181348457,
                  "midi": 58,
                  "cents_from_base": 90.45,
                  "prime_sources": [
                    8623,
                    8627,
                    8629,
                    8641,
                    17239,
                    17257,
                    34483,
                    34487,
                    34499,
                    34501,
                    34511,
                    34513,
                    34519,
                    34537,
                    34543,
                    34549
                  ]
                },
                {
                  "log_position": 0.176875,
                  "frequency": 248.6951760388849,
                  "midi": 59,
                  "cents_from_base": 212.25,
                  "prime_sources": [
                    9257,
                    18503,
                    18517,
                    18521,
                    18523,
                    18539,
                    18541,
                    36997,
                    37003,
                    37013,
                    37019,
                    37021,
                    37039,
                    37049,
                    37057,
                    37061,
                    37087
                  ]
                },
                {
                  "log_position": 0.43675,
                  "frequency": 297.78137534016145,
                  "midi": 62,
                  "cents_from_base": 524.1,
                  "prime_sources": [
                    11083,
                    11087,
                    11093,
                    22147,
                    22153,
                    22157,
                    22159,
                    22171,
                    22189,
                    22193,
                    44293,
                    44351,
                    44357,
                    44371,
                    44381,
                    44383,
                    44389
                  ]
                },
                {
                  "log_position": 0.610625,
                  "frequency": 335.9225217964596,
                  "midi": 64,
                  "cents_from_base": 732.75,
                  "prime_sources": [
                    6247,
                    6257,
                    12497,
                    12503,
                    12511,
                    12517,
                    24989,
                    25013,
                    25031,
                    25033,
                    25037,
                    49991,
                    49993,
                    49999,
                    50021,
                    50023,
                    50033,
                    50047,
                    50051,
                    50053,
                    50069,
                    50077,
                    50087,
                    50093,
                    50101
                  ]
                },
                {
                  "log_position": 0.6735,
                  "frequency": 350.88627652385884,
                  "midi": 65,
                  "cents_from_base": 808.1999999999999,
                  "prime_sources": [
                    6529,
                    13049,
                    13063,
                    26099,
                    26107,
                    26111,
                    26113,
                    26119,
                    26141,
                    26153,
                    26161,
                    52201,
                    52223,
                    52237,
                    52249,
                    52253,
                    52259,
                    52267,
                    52289,
                    52291,
                    52301,
                    52313,
                    52321
                  ]
                },
                {
                  "log_position": 0.958625,
                  "frequency": 427.56048438765623,
                  "midi": 69,
                  "cents_from_base": 1150.35,
                  "prime_sources": [
                    7951,
                    7963,
                    15901,
                    15907,
                    15913,
                    15919,
                    15923,
                    15937,
                    31799,
                    31817,
                    31847,
                    31849,
                    31859,
                    31873,
                    31883
                  ]
                },
                {
                  "log_position": 1.0,
                  "frequency": 440.0,
                  "midi": 69,
                  "cents_from_base": 1200.0,
                  "prime_sources": []
                }
              ]
            }
            ```

            `output/manifest.json`
            ```json
            {
              "scales": [
                "gap_scout_match_5_notes.json",
                "log_prime_scale_3_valley.json",
                "log_prime_scale_6_valley.json",
                "log_prime_scale_6_peak.json",
                "log_prime_scale_13_valley.json",
                "pure_prime_scale_128_primes.json",
                "sample_scale.json",
                "terrain_scale_8_valley.json"
              ]
            }
            ```

            `output/pure_prime_scale_128_primes.json`
            ```json
            {
              "name": "pure_prime_scale_128_primes",
              "base_frequency": 220.0,
              "notes": [
                {
                  "log_position": 0.0,
                  "frequency": 220.0,
                  "midi": 57,
                  "cents_from_base": 0.0,
                  "prime_sources": []
                },
                {
                  "log_position": 0.0,
                  "frequency": 220.0,
                  "midi": 57,
                  "cents_from_base": 0.0,
                  "prime_sources": []
                },
                {
                  "log_position": 0.5849625007211562,
                  "frequency": 330.0,
                  "midi": 64,
                  "cents_from_base": 701.9550008653874,
                  "prime_sources": []
                },
                {
                  "log_position": 0.32192809488736235,
                  "frequency": 275.0,
                  "midi": 61,
                  "cents_from_base": 386.3137138648348,
                  "prime_sources": []
                },
                {
                  "log_position": 0.8073549220576041,
                  "frequency": 385.0,
                  "midi": 67,
                  "cents_from_base": 968.8259064691249,
                  "prime_sources": []
                },
                {
                  "log_position": 0.45943161863729726,
                  "frequency": 302.5,
                  "midi": 63,
                  "cents_from_base": 551.3179423647567,
                  "prime_sources": []
                },
                {
                  "log_position": 0.7004397181410922,
                  "frequency": 357.5,
                  "midi": 65,
                  "cents_from_base": 840.5276617693106,
                  "prime_sources": []
                },
                {
                  "log_position": 0.0874628412503394,
                  "frequency": 233.75,
                  "midi": 58,
                  "cents_from_base": 104.95540950040728,
                  "prime_sources": []
                },
                {
                  "log_position": 0.2479275134435855,
                  "frequency": 261.25,
                  "midi": 60,
                  "cents_from_base": 297.5130161323026,
                  "prime_sources": []
                },
                {
                  "log_position": 0.5235619560570128,
                  "frequency": 316.25,
                  "midi": 63,
                  "cents_from_base": 628.2743472684155,
                  "prime_sources": []
                },
                {
                  "log_position": 0.8579809951275721,
                  "frequency": 398.75,
                  "midi": 67,
                  "cents_from_base": 1029.5771941530866,
                  "prime_sources": []
                },
                {
                  "log_position": 0.9541963103868752,
                  "frequency": 426.25,
                  "midi": 68,
                  "cents_from_base": 1145.0355724642502,
                  "prime_sources": []
                },
                {
                  "log_position": 0.20945336562894978,
                  "frequency": 254.375,
                  "midi": 60,
                  "cents_from_base": 251.34403875473973,
                  "prime_sources": []
                },
                {
                  "log_position": 0.3575520046180837,
                  "frequency": 281.875,
                  "midi": 61,
                  "cents_from_base": 429.0624055417004,
                  "prime_sources": []
                },
                {
                  "log_position": 0.42626475470209796,
                  "frequency": 295.625,
                  "midi": 62,
                  "cents_from_base": 511.51770564251757,
                  "prime_sources": []
                },
                {
                  "log_position": 0.5545888516776374,
                  "frequency": 323.125,
                  "midi": 64,
                  "cents_from_base": 665.5066220131648,
                  "prime_sources": []
                },
                {
                  "log_position": 0.7279204545631992,
                  "frequency": 364.375,
                  "midi": 66,
                  "cents_from_base": 873.504545475839,
                  "prime_sources": []
                },
                {
                  "log_position": 0.8826430493618412,
                  "frequency": 405.625,
                  "midi": 68,
                  "cents_from_base": 1059.1716592342095,
                  "prime_sources": []
                },
                {
                  "log_position": 0.9307373375628862,
                  "frequency": 419.375,
                  "midi": 68,
                  "cents_from_base": 1116.8848050754634,
                  "prime_sources": []
                },
                {
                  "log_position": 0.06608919045777244,
                  "frequency": 230.3125,
                  "midi": 58,
                  "cents_from_base": 79.30702854932693,
                  "prime_sources": []
                },
                {
                  "log_position": 0.14974711950468206,
                  "frequency": 244.0625,
                  "midi": 59,
                  "cents_from_base": 179.69654340561846,
                  "prime_sources": []
                },
                {
                  "log_position": 0.18982455888001723,
                  "frequency": 250.9375,
                  "midi": 59,
                  "cents_from_base": 227.78947065602068,
                  "prime_sources": []
                },
                {
                  "log_position": 0.30378074817710293,
                  "frequency": 271.5625,
                  "midi": 61,
                  "cents_from_base": 364.53689781252353,
                  "prime_sources": []
                },
                {
                  "log_position": 0.37503943134692475,
                  "frequency": 285.3125,
                  "midi": 62,
                  "cents_from_base": 450.04731761630967,
                  "prime_sources": []
                },
                {
                  "log_position": 0.47573343096639775,
                  "frequency": 305.9375,
                  "midi": 63,
                  "cents_from_base": 570.8801171596773,
                  "prime_sources": []
                },
                {
                  "log_position": 0.5999128421871277,
                  "frequency": 333.4375,
                  "midi": 64,
                  "cents_from_base": 719.8954106245533,
                  "prime_sources": []
                },
                {
                  "log_position": 0.6582114827517948,
                  "frequency": 347.1875,
                  "midi": 65,
                  "cents_from_base": 789.8537793021537,
                  "prime_sources": []
                },
                {
                  "log_position": 0.6865005271832184,
                  "frequency": 354.0625,
                  "midi": 65,
                  "cents_from_base": 823.8006326198621,
                  "prime_sources": []
                },
                {
                  "log_position": 0.7414669864011469,
                  "frequency": 367.8125,
                  "midi": 66,
                  "cents_from_base": 889.7603836813763,
                  "prime_sources": []
                },
                {
                  "log_position": 0.7681843247769263,
                  "frequency": 374.6875,
                  "midi": 66,
                  "cents_from_base": 921.8211897323116,
                  "prime_sources": []
                },
                {
                  "log_position": 0.8201789624151877,
                  "frequency": 388.4375,
                  "midi": 67,
                  "cents_from_base": 984.2147548982252,
                  "prime_sources": []
                },
                {
                  "log_position": 0.9886846867721658,
                  "frequency": 436.5625,
                  "midi": 69,
                  "cents_from_base": 1186.421624126599,
                  "prime_sources": []
                },
                {
                  "log_position": 0.03342300153745028,
                  "frequency": 225.15625,
                  "midi": 57,
                  "cents_from_base": 40.10760184494033,
                  "prime_sources": []
                },
                {
                  "log_position": 0.09803208296052672,
                  "frequency": 235.46875,
                  "midi": 58,
                  "cents_from_base": 117.63849955263207,
                  "prime_sources": []
                },
                {
                  "log_position": 0.11894107272350743,
                  "frequency": 238.90625,
                  "midi": 58,
                  "cents_from_base": 142.7292872682089,
                  "prime_sources": []
                },
                {
                  "log_position": 0.21916852046216156,
                  "frequency": 256.09375,
                  "midi": 60,
                  "cents_from_base": 263.00222455459385,
                  "prime_sources": []
                },
                {
                  "log_position": 0.2384047393250789,
                  "frequency": 259.53125,
                  "midi": 60,
                  "cents_from_base": 286.0856871900947,
                  "prime_sources": []
                },
                {
                  "log_position": 0.294620748891627,
                  "frequency": 269.84375,
                  "midi": 61,
                  "cents_from_base": 353.5448986699524,
                  "prime_sources": []
                },
                {
                  "log_position": 0.34872815423107756,
                  "frequency": 280.15625,
                  "midi": 61,
                  "cents_from_base": 418.4737850772931,
                  "prime_sources": []
                },
                {
                  "log_position": 0.38370429247405224,
                  "frequency": 287.03125,
                  "midi": 62,
                  "cents_from_base": 460.4451509688627,
                  "prime_sources": []
                },
                {
                  "log_position": 0.43462822763672465,
                  "frequency": 297.34375,
                  "midi": 62,
                  "cents_from_base": 521.5538731640696,
                  "prime_sources": []
                },
                {
                  "log_position": 0.4838157772642564,
                  "frequency": 307.65625,
                  "midi": 63,
                  "cents_from_base": 580.5789327171077,
                  "prime_sources": []
                },
                {
                  "log_position": 0.4998458870832054,
                  "frequency": 311.09375,
                  "midi": 63,
                  "cents_from_base": 599.8150644998465,
                  "prime_sources": []
                },
                {
                  "log_position": 0.5774288280357487,
                  "frequency": 328.28125,
                  "midi": 64,
                  "cents_from_base": 692.9145936428985,
                  "prime_sources": []
                },
                {
                  "log_position": 0.5924570372680804,
                  "frequency": 331.71875,
                  "midi": 64,
                  "cents_from_base": 710.9484447216965,
                  "prime_sources": []
                },
                {
                  "log_position": 0.6220518194563762,
                  "frequency": 338.59375,
                  "midi": 64,
                  "cents_from_base": 746.4621833476515,
                  "prime_sources": []
                },
                {
                  "log_position": 0.6366246205436489,
                  "frequency": 342.03125,
                  "midi": 65,
                  "cents_from_base": 763.9495446523787,
                  "prime_sources": []
                },
                {
                  "log_position": 0.7210991887071851,
                  "frequency": 362.65625,
                  "midi": 66,
                  "cents_from_base": 865.3190264486221,
                  "prime_sources": []
                },
                {
                  "log_position": 0.8008998999203047,
                  "frequency": 383.28125,
                  "midi": 67,
                  "cents_from_base": 961.0798799043657,
                  "prime_sources": []
                },
                {
                  "log_position": 0.826548487290915,
                  "frequency": 390.15625,
                  "midi": 67,
                  "cents_from_base": 991.858184749098,
                  "prime_sources": []
                },
                {
                  "log_position": 0.839203788096944,
                  "frequency": 393.59375,
                  "midi": 67,
                  "cents_from_base": 1007.0445457163328,
                  "prime_sources": []
                },
                {
                  "log_position": 0.8641861446542802,
                  "frequency": 400.46875,
                  "midi": 67,
                  "cents_from_base": 1037.0233735851364,
                  "prime_sources": []
                },
                {
                  "log_position": 0.9008668079807486,
                  "frequency": 410.78125,
                  "midi": 68,
                  "cents_from_base": 1081.0401695768983,
                  "prime_sources": []
                },
                {
                  "log_position": 0.9128893362299616,
                  "frequency": 414.21875,
                  "midi": 68,
                  "cents_from_base": 1095.467203475954,
                  "prime_sources": []
                },
                {
                  "log_position": 0.971543553950772,
                  "frequency": 431.40625,
                  "midi": 69,
                  "cents_from_base": 1165.8522647409263,
                  "prime_sources": []
                },
                {
                  "log_position": 0.005624549193878107,
                  "frequency": 220.859375,
                  "midi": 57,
                  "cents_from_base": 6.749459032653728,
                  "prime_sources": []
                },
                {
                  "log_position": 0.03891898929230235,
                  "frequency": 226.015625,
                  "midi": 57,
                  "cents_from_base": 46.70278715076282,
                  "prime_sources": []
                },
                {
                  "log_position": 0.07146236255662415,
                  "frequency": 231.171875,
                  "midi": 58,
                  "cents_from_base": 85.75483506794897,
                  "prime_sources": []
                },
                {
                  "log_position": 0.08214904135387156,
                  "frequency": 232.890625,
                  "midi": 58,
                  "cents_from_base": 98.57884962464587,
                  "prime_sources": []
                },
                {
                  "log_position": 0.11374216604918833,
                  "frequency": 238.046875,
                  "midi": 58,
                  "cents_from_base": 136.490599259026,
                  "prime_sources": []
                },
                {
                  "log_position": 0.1344263202209261,
                  "frequency": 241.484375,
                  "midi": 59,
                  "cents_from_base": 161.31158426511132,
                  "prime_sources": []
                },
                {
                  "log_position": 0.14465824283188233,
                  "frequency": 243.203125,
                  "midi": 59,
                  "cents_from_base": 173.5898913982588,
                  "prime_sources": []
                },
                {
                  "log_position": 0.19475685442224788,
                  "frequency": 251.796875,
                  "midi": 59,
                  "cents_from_base": 233.70822530669747,
                  "prime_sources": []
                },
                {
                  "log_position": 0.2620948453701794,
                  "frequency": 263.828125,
                  "midi": 60,
                  "cents_from_base": 314.5138144442153,
                  "prime_sources": []
                },
                {
                  "log_position": 0.28077077013060253,
                  "frequency": 267.265625,
                  "midi": 60,
                  "cents_from_base": 336.924924156723,
                  "prime_sources": []
                },
                {
                  "log_position": 0.2900188469326183,
                  "frequency": 268.984375,
                  "midi": 60,
                  "cents_from_base": 348.022616319142,
                  "prime_sources": []
                },
                {
                  "log_position": 0.3083390301394073,
                  "frequency": 272.421875,
                  "midi": 61,
                  "cents_from_base": 370.0068361672887,
                  "prime_sources": []
                },
                {
                  "log_position": 0.3706874068072177,
                  "frequency": 284.453125,
                  "midi": 61,
                  "cents_from_base": 444.82488816866123,
                  "prime_sources": []
                },
                {
                  "log_position": 0.3966047811818585,
                  "frequency": 289.609375,
                  "midi": 62,
                  "cents_from_base": 475.9257374182302,
                  "prime_sources": []
                },
                {
                  "log_position": 0.4387918525782609,
                  "frequency": 298.203125,
                  "midi": 62,
                  "cents_from_base": 526.5502230939131,
                  "prime_sources": []
                },
                {
                  "log_position": 0.44708322620965224,
                  "frequency": 299.921875,
                  "midi": 62,
                  "cents_from_base": 536.4998714515826,
                  "prime_sources": []
                },
                {
                  "log_position": 0.4635243732711803,
                  "frequency": 303.359375,
                  "midi": 63,
                  "cents_from_base": 556.2292479254163,
                  "prime_sources": []
                },
                {
                  "log_position": 0.48784003382305136,
                  "frequency": 308.515625,
                  "midi": 63,
                  "cents_from_base": 585.4080405876616,
                  "prime_sources": []
                },
                {
                  "log_position": 0.5196362528432128,
                  "frequency": 315.390625,
                  "midi": 63,
                  "cents_from_base": 623.5635034118553,
                  "prime_sources": []
                },
                {
                  "log_position": 0.5430318202552378,
                  "frequency": 320.546875,
                  "midi": 64,
                  "cents_from_base": 651.6381843062853,
                  "prime_sources": []
                },
                {
                  "log_position": 0.5660540381710917,
                  "frequency": 325.703125,
                  "midi": 64,
                  "cents_from_base": 679.26484580531,
                  "prime_sources": []
                },
                {
                  "log_position": 0.581200581924957,
                  "frequency": 329.140625,
                  "midi": 64,
                  "cents_from_base": 697.4406983099484,
                  "prime_sources": []
                },
                {
                  "log_position": 0.6036263449861919,
                  "frequency": 334.296875,
                  "midi": 64,
                  "cents_from_base": 724.3516139834303,
                  "prime_sources": []
                },
                {
                  "log_position": 0.6329951971429578,
                  "frequency": 341.171875,
                  "midi": 65,
                  "cents_from_base": 759.5942365715493,
                  "prime_sources": []
                },
                {
                  "log_position": 0.6474584264549202,
                  "frequency": 344.609375,
                  "midi": 65,
                  "cents_from_base": 776.9501117459043,
                  "prime_sources": []
                },
                {
                  "log_position": 0.6759570329417488,
                  "frequency": 351.484375,
                  "midi": 65,
                  "cents_from_base": 811.1484395300986,
                  "prime_sources": []
                },
                {
                  "log_position": 0.7108064336993516,
                  "frequency": 360.078125,
                  "midi": 66,
                  "cents_from_base": 852.9677204392219,
                  "prime_sources": []
                },
                {
                  "log_position": 0.7176764230663961,
                  "frequency": 361.796875,
                  "midi": 66,
                  "cents_from_base": 861.2117076796753,
                  "prime_sources": []
                },
                {
                  "log_position": 0.7515440590890982,
                  "frequency": 370.390625,
                  "midi": 66,
                  "cents_from_base": 901.8528709069178,
                  "prime_sources": []
                },
                {
                  "log_position": 0.7582232147267249,
                  "frequency": 372.109375,
                  "midi": 66,
                  "cents_from_base": 909.8678576720699,
                  "prime_sources": []
                },
                {
                  "log_position": 0.7780771295353582,
                  "frequency": 377.265625,
                  "midi": 66,
                  "cents_from_base": 933.6925554424299,
                  "prime_sources": []
                },
                {
                  "log_position": 0.7911628885550183,
                  "frequency": 380.703125,
                  "midi": 66,
                  "cents_from_base": 949.3954662660219,
                  "prime_sources": []
                },
                {
                  "log_position": 0.8105716347411469,
                  "frequency": 385.859375,
                  "midi": 67,
                  "cents_from_base": 972.6859616893763,
                  "prime_sources": []
                },
                {
                  "log_position": 0.8360503550580697,
                  "frequency": 392.734375,
                  "midi": 67,
                  "cents_from_base": 1003.2604260696836,
                  "prime_sources": []
                },
                {
                  "log_position": 0.848622940429338,
                  "frequency": 396.171875,
                  "midi": 67,
                  "cents_from_base": 1018.3475285152056,
                  "prime_sources": []
                },
                {
                  "log_position": 0.8548683832602364,
                  "frequency": 397.890625,
                  "midi": 67,
                  "cents_from_base": 1025.8420599122837,
                  "prime_sources": []
                },
                {
                  "log_position": 0.867278739709662,
                  "frequency": 401.328125,
                  "midi": 67,
                  "cents_from_base": 1040.7344876515945,
                  "prime_sources": []
                },
                {
                  "log_position": 0.9038818457361802,
                  "frequency": 411.640625,
                  "midi": 68,
                  "cents_from_base": 1084.6582148834163,
                  "prime_sources": []
                },
                {
                  "log_position": 0.9277779620823422,
                  "frequency": 418.515625,
                  "midi": 68,
                  "cents_from_base": 1113.3335544988106,
                  "prime_sources": []
                },
                {
                  "log_position": 0.939579214314693,
                  "frequency": 421.953125,
                  "midi": 68,
                  "cents_from_base": 1127.4950571776317,
                  "prime_sources": []
                },
                {
                  "log_position": 0.9628960053372605,
                  "frequency": 428.828125,
                  "midi": 69,
                  "cents_from_base": 1155.4752064047127,
                  "prime_sources": []
                },
                {
                  "log_position": 0.9744145898055271,
                  "frequency": 432.265625,
                  "midi": 69,
                  "cents_from_base": 1169.2975077666324,
                  "prime_sources": []
                },
                {
                  "log_position": 0.9915218460756953,
                  "frequency": 437.421875,
                  "midi": 69,
                  "cents_from_base": 1189.8262152908344,
                  "prime_sources": []
                },
                {
                  "log_position": 0.025139562278508228,
                  "frequency": 223.8671875,
                  "midi": 57,
                  "cents_from_base": 30.167474734209872,
                  "prime_sources": []
                },
                {
                  "log_position": 0.030667136246941375,
                  "frequency": 224.7265625,
                  "midi": 57,
                  "cents_from_base": 36.80056349632965,
                  "prime_sources": []
                },
                {
                  "log_position": 0.07948478382681526,
                  "frequency": 232.4609375,
                  "midi": 58,
                  "cents_from_base": 95.3817405921783,
                  "prime_sources": []
                },
                {
                  "log_position": 0.09539702279255656,
                  "frequency": 235.0390625,
                  "midi": 58,
                  "cents_from_base": 114.47642735106787,
                  "prime_sources": []
                },
                {
                  "log_position": 0.12153351734003176,
                  "frequency": 239.3359375,
                  "midi": 58,
                  "cents_from_base": 145.8402208080381,
                  "prime_sources": []
                },
                {
                  "log_position": 0.13699111208022957,
                  "frequency": 241.9140625,
                  "midi": 59,
                  "cents_from_base": 164.3893344962755,
                  "prime_sources": []
                },
                {
                  "log_position": 0.15228484230658193,
                  "frequency": 244.4921875,
                  "midi": 59,
                  "cents_from_base": 182.74181076789833,
                  "prime_sources": []
                },
                {
                  "log_position": 0.15734693536284278,
                  "frequency": 245.3515625,
                  "midi": 59,
                  "cents_from_base": 188.81632243541134,
                  "prime_sources": []
                },
                {
                  "log_position": 0.17242750864548248,
                  "frequency": 247.9296875,
                  "midi": 59,
                  "cents_from_base": 206.913010374579,
                  "prime_sources": []
                },
                {
                  "log_position": 0.1972166931100522,
                  "frequency": 252.2265625,
                  "midi": 59,
                  "cents_from_base": 236.66003173206263,
                  "prime_sources": []
                },
                {
                  "log_position": 0.21188829454600366,
                  "frequency": 254.8046875,
                  "midi": 60,
                  "cents_from_base": 254.2659534552044,
                  "prime_sources": []
                },
                {
                  "log_position": 0.22641219278878566,
                  "frequency": 257.3828125,
                  "midi": 60,
                  "cents_from_base": 271.6946313465428,
                  "prime_sources": []
                },
                {
                  "log_position": 0.23122118071118544,
                  "frequency": 258.2421875,
                  "midi": 60,
                  "cents_from_base": 277.46541685342254,
                  "prime_sources": []
                },
                {
                  "log_position": 0.24555270625568207,
                  "frequency": 260.8203125,
                  "midi": 60,
                  "cents_from_base": 294.6632475068185,
                  "prime_sources": []
                },
                {
                  "log_position": 0.2597432636907815,
                  "frequency": 263.3984375,
                  "midi": 60,
                  "cents_from_base": 311.6919164289378,
                  "prime_sources": []
                },
                {
                  "log_position": 0.2691266791494179,
                  "frequency": 265.1171875,
                  "midi": 60,
                  "cents_from_base": 322.9520149793015,
                  "prime_sources": []
                },
                {
                  "log_position": 0.27379559921426466,
                  "frequency": 265.9765625,
                  "midi": 60,
                  "cents_from_base": 328.5547190571176,
                  "prime_sources": []
                },
                {
                  "log_position": 0.301496194982549,
                  "frequency": 271.1328125,
                  "midi": 61,
                  "cents_from_base": 361.79543397905877,
                  "prime_sources": []
                },
                {
                  "log_position": 0.324180546618741,
                  "frequency": 275.4296875,
                  "midi": 61,
                  "cents_from_base": 389.0166559424892,
                  "prime_sources": []
                },
                {
                  "log_position": 0.32867492732794734,
                  "frequency": 276.2890625,
                  "midi": 61,
                  "cents_from_base": 394.4099127935368,
                  "prime_sources": []
                },
                {
                  "log_position": 0.3376219019925075,
                  "frequency": 278.0078125,
                  "midi": 61,
                  "cents_from_base": 405.14628239100904,
                  "prime_sources": []
                },
                {
                  "log_position": 0.3509391815464308,
                  "frequency": 280.5859375,
                  "midi": 61,
                  "cents_from_base": 421.12701785571693,
                  "prime_sources": []
                },
                {
                  "log_position": 0.36413465500805176,
                  "frequency": 283.1640625,
                  "midi": 61,
                  "cents_from_base": 436.9615860096621,
                  "prime_sources": []
                },
                {
                  "log_position": 0.3685064615076917,
                  "frequency": 284.0234375,
                  "midi": 61,
                  "cents_from_base": 442.20775380923,
                  "prime_sources": []
                },
                {
                  "log_position": 0.3944626946103171,
                  "frequency": 289.1796875,
                  "midi": 62,
                  "cents_from_base": 473.3552335323805,
                  "prime_sources": []
                },
                {
                  "log_position": 0.40301202357499677,
                  "frequency": 290.8984375,
                  "midi": 62,
                  "cents_from_base": 483.6144282899961,
                  "prime_sources": []
                },
                {
                  "log_position": 0.41574176829009046,
                  "frequency": 293.4765625,
                  "midi": 62,
                  "cents_from_base": 498.8901219481086,
                  "prime_sources": []
                },
                {
                  "log_position": 0.4325419003882585,
                  "frequency": 296.9140625,
                  "midi": 62,
                  "cents_from_base": 519.0502804659102,
                  "prime_sources": []
                },
                {
                  "log_position": 0.4532706340106232,
                  "frequency": 301.2109375,
                  "midi": 62,
                  "cents_from_base": 543.9247608127478,
                  "prime_sources": []
                },
                {
                  "log_position": 0.4696418172395161,
                  "frequency": 304.6484375,
                  "midi": 63,
                  "cents_from_base": 563.5701806874193,
                  "prime_sources": []
                },
                {
                  "log_position": 0.4898479604392978,
                  "frequency": 308.9453125,
                  "midi": 63,
                  "cents_from_base": 587.8175525271573,
                  "prime_sources": []
                },
                {
                  "log_position": 1.0,
                  "frequency": 440.0,
                  "midi": 69,
                  "cents_from_base": 1200.0,
                  "prime_sources": []
                }
              ]
            }
            ```

            `output/sample_scale.json`
            ```json
            {
              "name": "sample_scale",
              "base_frequency": 220.0,
              "notes": [
                {
                  "frequency": 220.0,
                  "cents_from_base": 0.0,
                  "midi": 57,
                  "log_position": 0.0,
                  "prime_sources": []
                },
                {
                  "frequency": 246.94,
                  "cents_from_base": 200.0,
                  "midi": 59,
                  "log_position": 0.1667,
                  "prime_sources": [
                    3
                  ]
                },
                {
                  "frequency": 261.63,
                  "cents_from_base": 300.0,
                  "midi": 60,
                  "log_position": 0.25,
                  "prime_sources": [
                    5
                  ]
                },
                {
                  "frequency": 293.66,
                  "cents_from_base": 500.0,
                  "midi": 62,
                  "log_position": 0.4167,
                  "prime_sources": [
                    7
                  ]
                },
                {
                  "frequency": 329.63,
                  "cents_from_base": 700.0,
                  "midi": 64,
                  "log_position": 0.5833,
                  "prime_sources": [
                    11
                  ]
                },
                {
                  "frequency": 392.0,
                  "cents_from_base": 900.0,
                  "midi": 67,
                  "log_position": 0.75,
                  "prime_sources": [
                    13
                  ]
                },
                {
                  "frequency": 440.0,
                  "cents_from_base": 1200.0,
                  "midi": 69,
                  "log_position": 1.0,
                  "prime_sources": []
                }
              ]
            }
            ```

            `output/terrain_scale_5_valley.json`
            ```json
            {
              "metadata": {
                "primes": [
                  2,
                  3,
                  5,
                  7,
                  11,
                  13,
                  17,
                  19,
                  23,
                  29,
                  31,
                  37,
                  41,
                  43,
                  47,
                  53,
                  59,
                  61,
                  67,
                  71,
                  73,
                  79,
                  83,
                  89,
                  97,
                  101,
                  103,
                  107,
                  109,
                  113,
                  127,
                  131,
                  137,
                  139,
                  149,
                  151,
                  157,
                  163,
                  167,
                  173,
                  179,
                  181,
                  191,
                  193,
                  197,
                  199,
                  211,
                  223,
                  227,
                  229,
                  233,
                  239,
                  241,
                  251,
                  257,
                  263,
                  269,
                  271,
                  277,
                  281,
                  283,
                  293,
                  307,
                  311,
                  313,
                  317,
                  331,
                  337,
                  347,
                  349,
                  353,
                  359,
                  367,
                  373,
                  379,
                  383,
                  389,
                  397,
                  401,
                  409,
                  419,
                  421,
                  431,
                  433,
                  439,
                  443,
                  449,
                  457,
                  461,
                  463,
                  467,
                  479,
                  487,
                  491,
                  499,
                  503,
                  509,
                  521,
                  523,
                  541
                ],
                "prime_count": 100,
                "linear_prime_positions": [
                  1.0,
                  1.5,
                  1.25,
                  1.75,
                  1.375,
                  1.625,
                  1.0625,
                  1.1875,
                  1.4375,
                  1.8125,
                  1.9375,
                  1.15625,
                  1.28125,
                  1.34375,
                  1.46875,
                  1.65625,
                  1.84375,
                  1.90625,
                  1.046875,
                  1.109375,
                  1.140625,
                  1.234375,
                  1.296875,
                  1.390625,
                  1.515625,
                  1.578125,
                  1.609375,
                  1.671875,
                  1.703125,
                  1.765625,
                  1.984375,
                  1.0234375,
                  1.0703125,
                  1.0859375,
                  1.1640625,
                  1.1796875,
                  1.2265625,
                  1.2734375,
                  1.3046875,
                  1.3515625,
                  1.3984375,
                  1.4140625,
                  1.4921875,
                  1.5078125,
                  1.5390625,
                  1.5546875,
                  1.6484375,
                  1.7421875,
                  1.7734375,
                  1.7890625,
                  1.8203125,
                  1.8671875,
                  1.8828125,
                  1.9609375,
                  1.00390625,
                  1.02734375,
                  1.05078125,
                  1.05859375,
                  1.08203125,
                  1.09765625,
                  1.10546875,
                  1.14453125,
                  1.19921875,
                  1.21484375,
                  1.22265625,
                  1.23828125,
                  1.29296875,
                  1.31640625,
                  1.35546875,
                  1.36328125,
                  1.37890625,
                  1.40234375,
                  1.43359375,
                  1.45703125,
                  1.48046875,
                  1.49609375,
                  1.51953125,
                  1.55078125,
                  1.56640625,
                  1.59765625,
                  1.63671875,
                  1.64453125,
                  1.68359375,
                  1.69140625,
                  1.71484375,
                  1.73046875,
                  1.75390625,
                  1.78515625,
                  1.80078125,
                  1.80859375,
                  1.82421875,
                  1.87109375,
                  1.90234375,
                  1.91796875,
                  1.94921875,
                  1.96484375,
                  1.98828125,
                  1.017578125,
                  1.021484375,
                  1.056640625
                ],
                "log_prime_positions": [
                  0.0,
                  0.5849625007211562,
                  0.32192809488736235,
                  0.8073549220576041,
                  0.45943161863729726,
                  0.7004397181410922,
                  0.0874628412503394,
                  0.2479275134435855,
                  0.5235619560570128,
                  0.8579809951275721,
                  0.9541963103868752,
                  0.20945336562894978,
                  0.3575520046180837,
                  0.42626475470209796,
                  0.5545888516776374,
                  0.7279204545631992,
                  0.8826430493618412,
                  0.9307373375628862,
                  0.06608919045777244,
                  0.14974711950468206,
                  0.18982455888001723,
                  0.30378074817710293,
                  0.37503943134692475,
                  0.47573343096639775,
                  0.5999128421871277,
                  0.6582114827517948,
                  0.6865005271832184,
                  0.7414669864011469,
                  0.7681843247769263,
                  0.8201789624151877,
                  0.9886846867721658,
                  0.03342300153745028,
                  0.09803208296052672,
                  0.11894107272350743,
                  0.21916852046216156,
                  0.2384047393250789,
                  0.294620748891627,
                  0.34872815423107756,
                  0.38370429247405224,
                  0.43462822763672465,
                  0.4838157772642564,
                  0.4998458870832054,
                  0.5774288280357487,
                  0.5924570372680804,
                  0.6220518194563762,
                  0.6366246205436489,
                  0.7210991887071851,
                  0.8008998999203047,
                  0.826548487290915,
                  0.839203788096944,
                  0.8641861446542802,
                  0.9008668079807486,
                  0.9128893362299616,
                  0.971543553950772,
                  0.005624549193878107,
                  0.03891898929230235,
                  0.07146236255662415,
                  0.08214904135387156,
                  0.11374216604918833,
                  0.1344263202209261,
                  0.14465824283188233,
                  0.19475685442224788,
                  0.2620948453701794,
                  0.28077077013060253,
                  0.2900188469326183,
                  0.3083390301394073,
                  0.3706874068072177,
                  0.3966047811818585,
                  0.4387918525782609,
                  0.44708322620965224,
                  0.4635243732711803,
                  0.48784003382305136,
                  0.5196362528432128,
                  0.5430318202552378,
                  0.5660540381710917,
                  0.581200581924957,
                  0.6036263449861919,
                  0.6329951971429578,
                  0.6474584264549202,
                  0.6759570329417488,
                  0.7108064336993516,
                  0.7176764230663961,
                  0.7515440590890982,
                  0.7582232147267249,
                  0.7780771295353582,
                  0.7911628885550183,
                  0.8105716347411469,
                  0.8360503550580697,
                  0.848622940429338,
                  0.8548683832602364,
                  0.867278739709662,
                  0.9038818457361802,
                  0.9277779620823422,
                  0.939579214314693,
                  0.9628960053372605,
                  0.9744145898055271,
                  0.9915218460756953,
                  0.025139562278508228,
                  0.030667136246941375,
                  0.07948478382681526
                ],
                "x_axis": [
                  0.0,
                  0.001,
                  0.002,
                  0.003,
                  0.004,
                  0.005,
                  0.006,
                  0.007,
                  0.008,
                  0.009,
                  0.01,
                  0.011,
                  0.012,
                  0.013,
                  0.014,
                  0.015,
                  0.016,
                  0.017,
                  0.018,
                  0.019,
                  0.02,
                  0.021,
                  0.022,
                  0.023,
                  0.024,
                  0.025,
                  0.026,
                  0.027,
                  0.028,
                  0.029,
                  0.03,
                  0.031,
                  0.032,
                  0.033,
                  0.034,
                  0.035,
                  0.036,
                  0.037,
                  0.038,
                  0.039,
                  0.04,
                  0.041,
                  0.042,
                  0.043,
                  0.044,
                  0.045,
                  0.046,
                  0.047,
                  0.048,
                  0.049,
                  0.05,
                  0.051,
                  0.052,
                  0.053,
                  0.054,
                  0.055,
                  0.056,
                  0.057,
                  0.058,
                  0.059,
                  0.06,
                  0.061,
                  0.062,
                  0.063,
                  0.064,
                  0.065,
                  0.066,
                  0.067,
                  0.068,
                  0.069,
                  0.07,
                  0.071,
                  0.072,
                  0.073,
                  0.074,
                  0.075,
                  0.076,
                  0.077,
                  0.078,
                  0.079,
                  0.08,
                  0.081,
                  0.082,
                  0.083,
                  0.084,
                  0.085,
                  0.086,
                  0.087,
                  0.088,
                  0.089,
                  0.09,
                  0.091,
                  0.092,
                  0.093,
                  0.094,
                  0.095,
                  0.096,
                  0.097,
                  0.098,
                  0.099,
                  0.1,
                  0.101,
                  0.102,
                  0.103,
                  0.104,
                  0.105,
                  0.106,
                  0.107,
                  0.108,
                  0.109,
                  0.11,
                  0.111,
                  0.112,
                  0.113,
                  0.114,
                  0.115,
                  0.116,
                  0.117,
                  0.118,
                  0.119,
                  0.12,
                  0.121,
                  0.122,
                  0.123,
                  0.124,
                  0.125,
                  0.126,
                  0.127,
                  0.128,
                  0.129,
                  0.13,
                  0.131,
                  0.132,
                  0.133,
                  0.134,
                  0.135,
                  0.136,
                  0.137,
                  0.138,
                  0.139,
                  0.14,
                  0.141,
                  0.142,
                  0.143,
                  0.144,
                  0.145,
                  0.146,
                  0.147,
                  0.148,
                  0.149,
                  0.15,
                  0.151,
                  0.152,
                  0.153,
                  0.154,
                  0.155,
                  0.156,
                  0.157,
                  0.158,
                  0.159,
                  0.16,
                  0.161,
                  0.162,
                  0.163,
                  0.164,
                  0.165,
                  0.166,
                  0.167,
                  0.168,
                  0.169,
                  0.17,
                  0.171,
                  0.172,
                  0.173,
                  0.174,
                  0.175,
                  0.176,
                  0.177,
                  0.178,
                  0.179,
                  0.18,
                  0.181,
                  0.182,
                  0.183,
                  0.184,
                  0.185,
                  0.186,
                  0.187,
                  0.188,
                  0.189,
                  0.19,
                  0.191,
                  0.192,
                  0.193,
                  0.194,
                  0.195,
                  0.196,
                  0.197,
                  0.198,
                  0.199,
                  0.2,
                  0.201,
                  0.202,
                  0.203,
                  0.204,
                  0.205,
                  0.206,
                  0.207,
                  0.208,
                  0.209,
                  0.21,
                  0.211,
                  0.212,
                  0.213,
                  0.214,
                  0.215,
                  0.216,
                  0.217,
                  0.218,
                  0.219,
                  0.22,
                  0.221,
                  0.222,
                  0.223,
                  0.224,
                  0.225,
                  0.226,
                  0.227,
                  0.228,
                  0.229,
                  0.23,
                  0.231,
                  0.232,
                  0.233,
                  0.234,
                  0.235,
                  0.236,
                  0.237,
                  0.238,
                  0.239,
                  0.24,
                  0.241,
                  0.242,
                  0.243,
                  0.244,
                  0.245,
                  0.246,
                  0.247,
                  0.248,
                  0.249,
                  0.25,
                  0.251,
                  0.252,
                  0.253,
                  0.254,
                  0.255,
                  0.256,
                  0.257,
                  0.258,
                  0.259,
                  0.26,
                  0.261,
                  0.262,
                  0.263,
                  0.264,
                  0.265,
                  0.266,
                  0.267,
                  0.268,
                  0.269,
                  0.27,
                  0.271,
                  0.272,
                  0.273,
                  0.274,
                  0.275,
                  0.276,
                  0.277,
                  0.278,
                  0.279,
                  0.28,
                  0.281,
                  0.282,
                  0.283,
                  0.284,
                  0.285,
                  0.286,
                  0.287,
                  0.288,
                  0.289,
                  0.29,
                  0.291,
                  0.292,
                  0.293,
                  0.294,
                  0.295,
                  0.296,
                  0.297,
                  0.298,
                  0.299,
                  0.3,
                  0.301,
                  0.302,
                  0.303,
                  0.304,
                  0.305,
                  0.306,
                  0.307,
                  0.308,
                  0.309,
                  0.31,
                  0.311,
                  0.312,
                  0.313,
                  0.314,
                  0.315,
                  0.316,
                  0.317,
                  0.318,
                  0.319,
                  0.32,
                  0.321,
                  0.322,
                  0.323,
                  0.324,
                  0.325,
                  0.326,
                  0.327,
                  0.328,
                  0.329,
                  0.33,
                  0.331,
                  0.332,
                  0.333,
                  0.334,
                  0.335,
                  0.336,
                  0.337,
                  0.338,
                  0.339,
                  0.34,
                  0.341,
                  0.342,
                  0.343,
                  0.344,
                  0.345,
                  0.346,
                  0.347,
                  0.348,
                  0.349,
                  0.35,
                  0.351,
                  0.352,
                  0.353,
                  0.354,
                  0.355,
                  0.356,
                  0.357,
                  0.358,
                  0.359,
                  0.36,
                  0.361,
                  0.362,
                  0.363,
                  0.364,
                  0.365,
                  0.366,
                  0.367,
                  0.368,
                  0.369,
                  0.37,
                  0.371,
                  0.372,
                  0.373,
                  0.374,
                  0.375,
                  0.376,
                  0.377,
                  0.378,
                  0.379,
                  0.38,
                  0.381,
                  0.382,
                  0.383,
                  0.384,
                  0.385,
                  0.386,
                  0.387,
                  0.388,
                  0.389,
                  0.39,
                  0.391,
                  0.392,
                  0.393,
                  0.394,
                  0.395,
                  0.396,
                  0.397,
                  0.398,
                  0.399,
                  0.4,
                  0.401,
                  0.402,
                  0.403,
                  0.404,
                  0.405,
                  0.406,
                  0.407,
                  0.408,
                  0.409,
                  0.41,
                  0.411,
                  0.412,
                  0.413,
                  0.414,
                  0.415,
                  0.416,
                  0.417,
                  0.418,
                  0.419,
                  0.42,
                  0.421,
                  0.422,
                  0.423,
                  0.424,
                  0.425,
                  0.426,
                  0.427,
                  0.428,
                  0.429,
                  0.43,
                  0.431,
                  0.432,
                  0.433,
                  0.434,
                  0.435,
                  0.436,
                  0.437,
                  0.438,
                  0.439,
                  0.44,
                  0.441,
                  0.442,
                  0.443,
                  0.444,
                  0.445,
                  0.446,
                  0.447,
                  0.448,
                  0.449,
                  0.45,
                  0.451,
                  0.452,
                  0.453,
                  0.454,
                  0.455,
                  0.456,
                  0.457,
                  0.458,
                  0.459,
                  0.46,
                  0.461,
                  0.462,
                  0.463,
                  0.464,
                  0.465,
                  0.466,
                  0.467,
                  0.468,
                  0.469,
                  0.47,
                  0.471,
                  0.472,
                  0.473,
                  0.474,
                  0.475,
                  0.476,
                  0.477,
                  0.478,
                  0.479,
                  0.48,
                  0.481,
                  0.482,
                  0.483,
                  0.484,
                  0.485,
                  0.486,
                  0.487,
                  0.488,
                  0.489,
                  0.49,
                  0.491,
                  0.492,
                  0.493,
                  0.494,
                  0.495,
                  0.496,
                  0.497,
                  0.498,
                  0.499,
                  0.5,
                  0.501,
                  0.502,
                  0.503,
                  0.504,
                  0.505,
                  0.506,
                  0.507,
                  0.508,
                  0.509,
                  0.51,
                  0.511,
                  0.512,
                  0.513,
                  0.514,
                  0.515,
                  0.516,
                  0.517,
                  0.518,
                  0.519,
                  0.52,
                  0.521,
                  0.522,
                  0.523,
                  0.524,
                  0.525,
                  0.526,
                  0.527,
                  0.528,
                  0.529,
                  0.53,
                  0.531,
                  0.532,
                  0.533,
                  0.534,
                  0.535,
                  0.536,
                  0.537,
                  0.538,
                  0.539,
                  0.54,
                  0.541,
                  0.542,
                  0.543,
                  0.544,
                  0.545,
                  0.546,
                  0.547,
                  0.548,
                  0.549,
                  0.55,
                  0.551,
                  0.552,
                  0.553,
                  0.554,
                  0.555,
                  0.556,
                  0.557,
                  0.558,
                  0.559,
                  0.56,
                  0.561,
                  0.562,
                  0.563,
                  0.564,
                  0.565,
                  0.566,
                  0.567,
                  0.568,
                  0.569,
                  0.57,
                  0.571,
                  0.572,
                  0.573,
                  0.574,
                  0.575,
                  0.576,
                  0.577,
                  0.578,
                  0.579,
                  0.58,
                  0.581,
                  0.582,
                  0.583,
                  0.584,
                  0.585,
                  0.586,
                  0.587,
                  0.588,
                  0.589,
                  0.59,
                  0.591,
                  0.592,
                  0.593,
                  0.594,
                  0.595,
                  0.596,
                  0.597,
                  0.598,
                  0.599,
                  0.6,
                  0.601,
                  0.602,
                  0.603,
                  0.604,
                  0.605,
                  0.606,
                  0.607,
                  0.608,
                  0.609,
                  0.61,
                  0.611,
                  0.612,
                  0.613,
                  0.614,
                  0.615,
                  0.616,
                  0.617,
                  0.618,
                  0.619,
                  0.62,
                  0.621,
                  0.622,
                  0.623,
                  0.624,
                  0.625,
                  0.626,
                  0.627,
                  0.628,
                  0.629,
                  0.63,
                  0.631,
                  0.632,
                  0.633,
                  0.634,
                  0.635,
                  0.636,
                  0.637,
                  0.638,
                  0.639,
                  0.64,
                  0.641,
                  0.642,
                  0.643,
                  0.644,
                  0.645,
                  0.646,
                  0.647,
                  0.648,
                  0.649,
                  0.65,
                  0.651,
                  0.652,
                  0.653,
                  0.654,
                  0.655,
                  0.656,
                  0.657,
                  0.658,
                  0.659,
                  0.66,
                  0.661,
                  0.662,
                  0.663,
                  0.664,
                  0.665,
                  0.666,
                  0.667,
                  0.668,
                  0.669,
                  0.67,
                  0.671,
                  0.672,
                  0.673,
                  0.674,
                  0.675,
                  0.676,
                  0.677,
                  0.678,
                  0.679,
                  0.68,
                  0.681,
                  0.682,
                  0.683,
                  0.684,
                  0.685,
                  0.686,
                  0.687,
                  0.688,
                  0.689,
                  0.69,
                  0.691,
                  0.692,
                  0.693,
                  0.694,
                  0.695,
                  0.696,
                  0.697,
                  0.698,
                  0.699,
                  0.7,
                  0.701,
                  0.702,
                  0.703,
                  0.704,
                  0.705,
                  0.706,
                  0.707,
                  0.708,
                  0.709,
                  0.71,
                  0.711,
                  0.712,
                  0.713,
                  0.714,
                  0.715,
                  0.716,
                  0.717,
                  0.718,
                  0.719,
                  0.72,
                  0.721,
                  0.722,
                  0.723,
                  0.724,
                  0.725,
                  0.726,
                  0.727,
                  0.728,
                  0.729,
                  0.73,
                  0.731,
                  0.732,
                  0.733,
                  0.734,
                  0.735,
                  0.736,
                  0.737,
                  0.738,
                  0.739,
                  0.74,
                  0.741,
                  0.742,
                  0.743,
                  0.744,
                  0.745,
                  0.746,
                  0.747,
                  0.748,
                  0.749,
                  0.75,
                  0.751,
                  0.752,
                  0.753,
                  0.754,
                  0.755,
                  0.756,
                  0.757,
                  0.758,
                  0.759,
                  0.76,
                  0.761,
                  0.762,
                  0.763,
                  0.764,
                  0.765,
                  0.766,
                  0.767,
                  0.768,
                  0.769,
                  0.77,
                  0.771,
                  0.772,
                  0.773,
                  0.774,
                  0.775,
                  0.776,
                  0.777,
                  0.778,
                  0.779,
                  0.78,
                  0.781,
                  0.782,
                  0.783,
                  0.784,
                  0.785,
                  0.786,
                  0.787,
                  0.788,
                  0.789,
                  0.79,
                  0.791,
                  0.792,
                  0.793,
                  0.794,
                  0.795,
                  0.796,
                  0.797,
                  0.798,
                  0.799,
                  0.8,
                  0.801,
                  0.802,
                  0.803,
                  0.804,
                  0.805,
                  0.806,
                  0.807,
                  0.808,
                  0.809,
                  0.81,
                  0.811,
                  0.812,
                  0.813,
                  0.814,
                  0.815,
                  0.816,
                  0.817,
                  0.818,
                  0.819,
                  0.82,
                  0.821,
                  0.822,
                  0.823,
                  0.824,
                  0.825,
                  0.826,
                  0.827,
                  0.828,
                  0.829,
                  0.83,
                  0.831,
                  0.832,
                  0.833,
                  0.834,
                  0.835,
                  0.836,
                  0.837,
                  0.838,
                  0.839,
                  0.84,
                  0.841,
                  0.842,
                  0.843,
                  0.844,
                  0.845,
                  0.846,
                  0.847,
                  0.848,
                  0.849,
                  0.85,
                  0.851,
                  0.852,
                  0.853,
                  0.854,
                  0.855,
                  0.856,
                  0.857,
                  0.858,
                  0.859,
                  0.86,
                  0.861,
                  0.862,
                  0.863,
                  0.864,
                  0.865,
                  0.866,
                  0.867,
                  0.868,
                  0.869,
                  0.87,
                  0.871,
                  0.872,
                  0.873,
                  0.874,
                  0.875,
                  0.876,
                  0.877,
                  0.878,
                  0.879,
                  0.88,
                  0.881,
                  0.882,
                  0.883,
                  0.884,
                  0.885,
                  0.886,
                  0.887,
                  0.888,
                  0.889,
                  0.89,
                  0.891,
                  0.892,
                  0.893,
                  0.894,
                  0.895,
                  0.896,
                  0.897,
                  0.898,
                  0.899,
                  0.9,
                  0.901,
                  0.902,
                  0.903,
                  0.904,
                  0.905,
                  0.906,
                  0.907,
                  0.908,
                  0.909,
                  0.91,
                  0.911,
                  0.912,
                  0.913,
                  0.914,
                  0.915,
                  0.916,
                  0.917,
                  0.918,
                  0.919,
                  0.92,
                  0.921,
                  0.922,
                  0.923,
                  0.924,
                  0.925,
                  0.926,
                  0.927,
                  0.928,
                  0.929,
                  0.93,
                  0.931,
                  0.932,
                  0.933,
                  0.934,
                  0.935,
                  0.936,
                  0.937,
                  0.938,
                  0.939,
                  0.94,
                  0.941,
                  0.942,
                  0.943,
                  0.944,
                  0.945,
                  0.946,
                  0.947,
                  0.948,
                  0.949,
                  0.95,
                  0.951,
                  0.952,
                  0.953,
                  0.954,
                  0.955,
                  0.956,
                  0.957,
                  0.958,
                  0.959,
                  0.96,
                  0.961,
                  0.962,
                  0.963,
                  0.964,
                  0.965,
                  0.966,
                  0.967,
                  0.968,
                  0.969,
                  0.97,
                  0.971,
                  0.972,
                  0.973,
                  0.974,
                  0.975,
                  0.976,
                  0.977,
                  0.978,
                  0.979,
                  0.98,
                  0.981,
                  0.982,
                  0.983,
                  0.984,
                  0.985,
                  0.986,
                  0.987,
                  0.988,
                  0.989,
                  0.99,
                  0.991,
                  0.992,
                  0.993,
                  0.994,
                  0.995,
                  0.996,
                  0.997,
                  0.998,
                  0.999
                ],
                "density_map": [
                  0.5,
                  0.4933476736006886,
                  0.4567413375486747,
                  0.3942183596576802,
                  0.3216486915168152,
                  0.25386971177161305,
                  0.0038850477825144083,
                  0.003742508194591678,
                  0.0033671983590304157,
                  0.002830968519586001,
                  0.0022670349229450704,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0.0011821215475430824,
                  0.0014624711715632845,
                  0.0017140727400161864,
                  0.0018729402503653845,
                  0.0019191359916943041,
                  0.0029342406381951255,
                  0.003078929394702555,
                  0.003121583775363517,
                  0.007453581219555391,
                  0.008393880381643869,
                  0.008470869569816812,
                  0.00916177691215584,
                  0.0092822659953349,
                  0.010942232759534643,
                  0.010817840641006837,
                  0.009427689579732928,
                  0.00881174772256039,
                  0.007984815405870609,
                  0.003802154322880201,
                  0.0037213985710763324,
                  0.0034200761979424083,
                  0.002929196417612764,
                  0.0023736688420688532,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0.009300000406114898,
                  0.011480656977717026,
                  0.013411788315280032,
                  0.014601968698773357,
                  0.014924738859155273,
                  0.016838222609716205,
                  0.016346592868180465,
                  0.015035605911637117,
                  0.013238266817162146,
                  0.011338390835019658,
                  0.0037034309582573838,
                  0.0035322222634712967,
                  0.003141068912348472,
                  0.0036650387156374918,
                  0.00339820072158475,
                  0.0015743380098329036,
                  0.004031321051130039,
                  0.004649593946058082,
                  0.0051335581928198286,
                  0.005358401497688046,
                  0.0052566281658642505,
                  0.03851556982320608,
                  0.04648920984568961,
                  0.053227145584218774,
                  0.05864730527790425,
                  0.06058534688863152,
                  0.0586018410546362,
                  0.05589439018355271,
                  0.049706430428010914,
                  0.04139786595507199,
                  0.032965527737689876,
                  0,
                  0.004608180635179286,
                  0.005674315663458574,
                  0.006603881070455419,
                  0.007160653809822722,
                  0.007299245999501241,
                  0.007180871227852606,
                  0.0066527348783720405,
                  0.005740861152901491,
                  0.004675949907370306,
                  0.003679001496315823,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0.0019243383341630556,
                  0.002431705801464039,
                  0.002952460394425129,
                  0.0033686953382975164,
                  0.0035797220603035547,
                  0.00725835497314597,
                  0.008135753768824378,
                  0.008860563921983559,
                  0.009265394663002642,
                  0.009248148799350063,
                  0.007194136125593681,
                  0.007048748179194045,
                  0.006488244574678364,
                  0.005565067477635061,
                  0.004514037603895834,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0.002048343582109583,
                  0.002562576016697192,
                  0.0030572179920493633,
                  0.00341048947808024,
                  0.0035511803159839557,
                  0.003542920564723507,
                  0.003371361311137437,
                  0.002990291701284893,
                  0.002485345441384244,
                  0.001976763773731445,
                  0.0019227370788580831,
                  0.0024237639898976827,
                  0.0029297667439583024,
                  0.0033230768552521164,
                  0.003511487259153485,
                  0.011027737115296619,
                  0.01288332250255701,
                  0.014581628980052035,
                  0.01572474447476769,
                  0.016039322237071604,
                  0.01407640946287026,
                  0.013655315793683502,
                  0.01239531870404901,
                  0.010499968488018999,
                  0.008447791458182176,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0.007154922002951435,
                  0.009061647062567553,
                  0.01104856058872992,
                  0.012678756517393783,
                  0.01354899409045495,
                  0.015508156950073678,
                  0.015632689951657182,
                  0.01496242750645236,
                  0.013546755381987657,
                  0.011749507743486832,
                  0.0034111904023104776,
                  0.0033109157392743277,
                  0.003007527712053966,
                  0.002549204082034914,
                  0.0020517666396954034,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0.015455678926353687,
                  0.019354184672609354,
                  0.023126751295448698,
                  0.02584951694584969,
                  0.026960281695529952,
                  0.026920636575190015,
                  0.025661422763317177,
                  0.022804995509628223,
                  0.018982904221798453,
                  0.015111586130319552,
                  0.004105732787707358,
                  0.005085631632515325,
                  0.005971668708302011,
                  0.006538761499824257,
                  0.006710010034984284,
                  0.006636567050277145,
                  0.006207344970372332,
                  0.005406634555805857,
                  0.004432801667679778,
                  0.0034994303452182685,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0.0038315671653723574,
                  0.004789779450121053,
                  0.005707024209985212,
                  0.0063565742300565565,
                  0.006610193238373379,
                  0.006590287519033538,
                  0.006262437750385111,
                  0.005546027803173151,
                  0.004603987239094569,
                  0.030455468488487205,
                  0.034024978016097815,
                  0.04169450683211657,
                  0.04818542756443097,
                  0.05186292209296099,
                  0.05263024710118889,
                  0.05153347349536338,
                  0.0473896862369698,
                  0.04061060989060068,
                  0.03292106314908909,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0.002026997801968945,
                  0.002502903328600359,
                  0.0029249913694859415,
                  0.00318584937703481,
                  0.0032571675709386016,
                  0.003212533977763555,
                  0.00298941987905486,
                  0.002590662091441473,
                  0.0021163834187149727,
                  0.0016676458416065854,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0.001701922041406249,
                  0.0021523575152366885,
                  0.0026171529180656953,
                  0.0029920992556283824,
                  0.003185711020894571,
                  0.0032139876543007934,
                  0.0031218776559434748,
                  0.002838664228607196,
                  0.0024081784880493084,
                  0.0019393409283885365,
                  0.0020231053133021436,
                  0.0024896750497658197,
                  0.0028949858018192222,
                  0.003136107010004632,
                  0.006692602268170207,
                  0.007545425794757989,
                  0.00822026568596236,
                  0.0085166857142981,
                  0.008375553143881708,
                  0.007964335348485662,
                  0.0061246530069200495,
                  0.005508940781263593,
                  0.004630579316680752,
                  0.010391140371229443,
                  0.008454676462621833,
                  0.010285692557443946,
                  0.01176746103339487,
                  0.012537429515167557,
                  0.014507077958182749,
                  0.014609132303435416,
                  0.013933488001473423,
                  0.012540358008423076,
                  0.010803303977776398,
                  0.0031346573488521077,
                  0.0029659312397592877,
                  0.0026143864655111667,
                  0.0021625354475961487,
                  0.0017153679477460962,
                  0,
                  0,
                  0,
                  0.10181048110133709,
                  0.1292779994536873,
                  0.15842277716411246,
                  0.18309295777552154,
                  0.1970745911289608,
                  0.1999950398633511,
                  0.1958327348506088,
                  0.18009338548403084,
                  0.1543369923297864,
                  0.12511676275359288,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0.003281488486214009,
                  0.004145037711775666,
                  0.0050290295590755775,
                  0.005732376575590579,
                  0.006085714924660379,
                  0.006130743664749135,
                  0.005941091839458617,
                  0.005385508682431323,
                  0.004556628824958896,
                  0.017282852466623148,
                  0.01711161245756978,
                  0.020563156283440454,
                  0.02314769018458414,
                  0.02429186710885055,
                  0.02433177396818675,
                  0.023336979106973535,
                  0.02088695049356051,
                  0.01748524744015399,
                  0.013965817453709777,
                  0,
                  0,
                  0,
                  0.0016322104006102184,
                  0.002059313920635553,
                  0.00249312529598663,
                  0.002833660542384466,
                  0.0030001224294577632,
                  0.010611699622267096,
                  0.012271509133495293,
                  0.013528412794712457,
                  0.014041279455960017,
                  0.013834826151277343,
                  0.01185639277588225,
                  0.010990082171015407,
                  0.00948839532625382,
                  0.01095270486792018,
                  0.01015047538508011,
                  0.004927871117571012,
                  0.005607645541985816,
                  0.005943763167868281,
                  0.0059829348026568755,
                  0.005790086712115553,
                  0.00523957460689999,
                  0.004426610389174422,
                  0.0035554823450816408,
                  0,
                  0,
                  0,
                  0.0016358553437173175,
                  0.00205875172587628,
                  0.002481306228375666,
                  0.0028037334441173394,
                  0.002952336746161855,
                  0.0029621557737574593,
                  0.002850127349116709,
                  0.0025606464754129314,
                  0.002150313602582188,
                  0.0017207271198690036,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0.013909740901067896,
                  0.01729687408290226,
                  0.02043426873474404,
                  0.02253076604534723,
                  0.023240819327807118,
                  0.023064564201037595,
                  0.021715043692735907,
                  0.019041182491534473,
                  0.018856794724228694,
                  0.0164078868201797,
                  0.004815656474744258,
                  0.005450509427756418,
                  0.007265617387476515,
                  0.0076917933798666075,
                  0.00789840919280671,
                  0.007680841804517996,
                  0.007062028299937705,
                  0.006251572502576084,
                  0.002801444241216976,
                  0.002551180783375906,
                  0.0021671755096714534,
                  0.0035345894637894663,
                  0.0022064773970720845,
                  0.0025766168042093674,
                  0.0028040716288367513,
                  0.002865227092998433,
                  0.002824666676649579,
                  0.002626352988386056,
                  0.0022742239029817203,
                  0.0018568410370701717,
                  0.0014627200357871985,
                  0,
                  0,
                  0.05225943409193625,
                  0.06539132406610251,
                  0.0780378875403259,
                  0.08708872230795368,
                  0.0923029854617042,
                  0.09251373170097206,
                  0.08855950239070605,
                  0.07914568298749484,
                  0.06638306481352386,
                  0.05338734469687315,
                  0.0027048748981324745,
                  0.002416087286954145,
                  0.002019342151333304,
                  0.0016113466884748677,
                  0,
                  0,
                  0.006002121606371323,
                  0.007582761409350084,
                  0.009202436676137545,
                  0.010493353796438917,
                  0.011144117823129273,
                  0.011228585789137942,
                  0.010884432698950614,
                  0.009870336731260039,
                  0.011278218462511464,
                  0.010420278782187447,
                  0.004512607082493473,
                  0.005175285521587032,
                  0.00697649761322138,
                  0.007421449065775958,
                  0.007678814246588905,
                  0.007534920396995043,
                  0.006974233980993687,
                  0.006190141603224164,
                  0.0027151304990402645,
                  0.0024811810742217627,
                  0.002114199314285436,
                  0.0017074463370582384,
                  0,
                  0,
                  0.002870482108133419,
                  0.0036374595564928206,
                  0.0044397436779018236,
                  0.005102332803799573,
                  0.005460579094856124,
                  0.005523940534936131,
                  0.005386969500824638,
                  0.004924875479243524,
                  0.004198035288147317,
                  0.0033912044083267323,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0.0014906468256706325,
                  0.0018778291203191927,
                  0.0022671556398400792,
                  0.0025675017776269214,
                  0.026928904562838703,
                  0.0331604624966375,
                  0.03922280363017666,
                  0.04359130050748047,
                  0.045282046320960195,
                  0.044971687531754095,
                  0.04163143168672088,
                  0.03728752384822393,
                  0.031233016064029086,
                  0.024955144057061913,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0.00169265056184588,
                  0.0020842325222158115,
                  0.002425628852248647,
                  0.002630084248910994,
                  0.002680956485338957,
                  0.0026374491378699434,
                  0.002443425560537778,
                  0.0021084740452144875,
                  0.0017173378829870892,
                  0.0013511800476149025,
                  0,
                  0.011775007176621161,
                  0.014811625952983092,
                  0.017835955317617596,
                  0.020130707111154434,
                  0.021175802908222657,
                  0.021235420881145006,
                  0.020412803494218423,
                  0.018318426762358488,
                  0.015368397264584062,
                  0.0122910659276548,
                  0,
                  0,
                  0.001657401838994899,
                  0.002042860489498348,
                  0.002380978273223985,
                  0.0025857624667499066,
                  0.0026384903882076464,
                  0.00259807318425849,
                  0.0024107203808786705,
                  0.002083373088001061,
                  0.00169866089094211,
                  0.00133717973729363,
                  0,
                  0.003011720388245123,
                  0.0037681414856586266,
                  0.004496153427712656,
                  0.005016606714643822,
                  0.006809713682516232,
                  0.0071789537444136315,
                  0.007274651324571593,
                  0.1751752467538875,
                  0.22006550105074046,
                  0.26791580608721943,
                  0.3064158446196641,
                  0.33011547565459565,
                  0.3350684780610361,
                  0.32829365478547845,
                  0.3013855271130692,
                  0.26182976615109416,
                  0.21388734636463874,
                  0.00443123067040312,
                  0.004954241063258527,
                  0.005168291424435637,
                  0.005161290502540415,
                  0.004921020429240131,
                  0.009642330697279383,
                  0.010328713604252776,
                  0.011087822568804664,
                  0.009453492454599222,
                  0.011574266326261285,
                  0.012084244232771336,
                  0.012229221389361843,
                  0.011690501515036963,
                  0.010489443805054916,
                  0.008993495996769104,
                  0.002472864656804275,
                  0.0022251673457726936,
                  0.0018710090901718631,
                  0.001498399782121939,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0.003190227971173354,
                  0.003931784461802426,
                  0.004581870527471627,
                  0.004975162163618727,
                  0.005076086626463529,
                  0.004997873481472535,
                  0.004636741314401794,
                  0.004006525611957252,
                  0.0032663459179133815,
                  0.002571121134195797,
                  0.0012609588044560996,
                  0.0016036576199745614,
                  0.0019713647332113616,
                  0.0022886813338288425,
                  0.005232044649548849,
                  0.005990633422821037,
                  0.006662971707801042,
                  0.00702603545835785,
                  0.006965486469818833,
                  0.006617533505342603,
                  0.00483331340503622,
                  0.004348636817063228,
                  0.0036561275588846615,
                  0.0029278285863617156,
                  0,
                  0.0014243511008749997,
                  0.001783940064822472,
                  0.002132300432734597,
                  0.002384210891905388,
                  0.0024874341712605354,
                  0.0024841737760615923,
                  0.002368738877183716,
                  0.002105833484201892,
                  0.0017533994844931655,
                  0.0013960471557607484,
                  0,
                  0.0059965214140442,
                  0.007440842832425693,
                  0.008761147526189405,
                  0.009622907142211765,
                  0.009897348591266683,
                  0.009804159338223862,
                  0.0091971694425377,
                  0.008034704043005549,
                  0.006601783870480708,
                  0.005217667754871245,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0.0012356818659999315,
                  0.0015701334808781002,
                  0.001926739000234981,
                  0.002231143408022157,
                  0.0024064165867925223,
                  0.0024449710376702022,
                  0.0023973466182009235,
                  0.0022092283780027143,
                  0.0018968878220596164,
                  0.001539732882490508,
                  0,
                  0.005489322891611404,
                  0.006885054441921638,
                  0.008249627111031003,
                  0.009252247214650547,
                  0.009678052439856774,
                  0.009678213275396712,
                  0.009253011069782324,
                  0.00825093385719822,
                  0.00688656228352338,
                  0.005490720259188219,
                  0,
                  0,
                  0,
                  0,
                  0.04413367131147935,
                  0.0552394661081511,
                  0.06595410425497165,
                  0.0736464969260725,
                  0.07674705261197245,
                  0.07660109878053364,
                  0.07295450069776574,
                  0.06477042206893437,
                  0.05387356781387518,
                  0.04286775699656782,
                  0.0012521636527764149,
                  0.0015850939665460037,
                  0.0019308919320247847,
                  0.0022130094212994738,
                  0.002361959169697026,
                  0.002385931274898922,
                  0.0023219874210932663,
                  0.003403522602114844,
                  0.0034227469125470028,
                  0.0034151798007402137,
                  0.0022301310671377656,
                  0.005305694660332506,
                  0.006011474018344476,
                  0.006546179307328828,
                  0.006704803987590918,
                  0.006485310276155213,
                  0.006076022186789797,
                  0.013974623928018988,
                  0.015989248172467056,
                  0.018048087613967107,
                  0.01971636250326601,
                  0.018597506528117504,
                  0.018867322213643036,
                  0.01846789261014279,
                  0.016974323429884614,
                  0.014539414349556969,
                  0.01178274453903008,
                  0,
                  0,
                  0,
                  0,
                  0.005327008047715246,
                  0.006673830842746722,
                  0.007981048413977423,
                  0.008929438825933871,
                  0.009320946155955055,
                  0.009311245947046598,
                  0.008883393253103835,
                  0.007902279752351719,
                  0.006582939277743584,
                  0.0052427739707893925,
                  0.0012980923782948141,
                  0.0016305033369541008,
                  0.001958510323744454,
                  0.002203415634705336,
                  0.0023111591019320857,
                  0.0023143742254133964,
                  0.0022186712908751367,
                  0.0033794948051774016,
                  0.0033923001203263106,
                  0.003366465958188198,
                  0.002243067892383514,
                  0.002308496721234805,
                  0.0022877053822158515,
                  0.0021477896422434175,
                  0.001877857066118707,
                  0.0015438815539218953,
                  0.0012205839791383036,
                  0.0055917877365997395,
                  0.006930903950213077,
                  0.008146656701303552,
                  0.008930460182889186,
                  0.009171918641294376,
                  0.00907674596129615,
                  0.008498951285528411,
                  0.0074107406987986065,
                  0.006080741367265403,
                  0.004802374235076821,
                  0.0014233090678875391,
                  0.0017561175970413092,
                  0.0020498888846447474,
                  0.0022298729610228493,
                  0.0022778370071944772,
                  0.002245045504854621,
                  0.002086533626412668,
                  0.0018060321357791316,
                  0.0014741460946386604,
                  0.0011610822433030926,
                  0,
                  0,
                  0,
                  0.0013827463903794215,
                  0.0017123579653489016,
                  0.0020099652771815306,
                  0.002199946846204788,
                  0.002256904013979241,
                  0.002231740066279509,
                  0.002086590197460617,
                  0.0018167254102469952,
                  0.0014890824533179306,
                  0.0034741881857478524,
                  0.0029170197814308986,
                  0.003569816181006497,
                  0.004117809899187263,
                  0.00442351550204387,
                  0.004484050641403822,
                  0.004384741586832451,
                  0.08766479856113372,
                  0.10780965218616599,
                  0.12676972624150495,
                  0.13883506749958976,
                  0.1442217050792369,
                  0.14388014483792944,
                  0.13661560845396484,
                  0.1209138440562995,
                  0.10048862916207885,
                  0.08011824253849235,
                  0.0019127462674948643,
                  0.0016030803757262873,
                  0.0012812971601870332,
                  0.005400598455565182,
                  0.006692443184993616,
                  0.00786367555310426,
                  0.008616921467131309,
                  0.00884741317110432,
                  0.008753907616883844,
                  0.01065565587499951,
                  0.010234794704616869,
                  0.009574603201085672,
                  0.008808301812318908,
                  0.0043877984267666915,
                  0.004394517696263,
                  0.004213941990992432,
                  0.003770585400783453,
                  0.0031558481462126754,
                  0.002520329637546562,
                  0.0013756802979105658,
                  0.0016953413379064905,
                  0.001975460081053357,
                  0.004794322435288835,
                  0.005474813557399351,
                  0.006022266165959238,
                  0.006244493957117974,
                  0.006091998112082986,
                  0.005730631695874504,
                  0.005161218722712215,
                  0.0035390789112271473,
                  0.0029067781493571513,
                  0.00348743202781065,
                  0.0014991846140754472,
                  0.0018086927584041765,
                  0.002046364570549017,
                  0.0021573773988166687,
                  0.0021658150257202083,
                  0.0032020643544162855,
                  0.0032916183486372307,
                  0.0033065796379749234,
                  0.020576771714793014,
                  0.024157462427609806,
                  0.029216356774828416,
                  0.033490473047676196,
                  0.035835367197465995,
                  0.036130880458583196,
                  0.03518074470520655,
                  0.033860097687732876,
                  0.030111765867769497,
                  0.025645005483794538,
                  0.005453894211962317,
                  0.0058789715589818055,
                  0.006124448690128843,
                  0.006049403303462457,
                  0.005607661335753866,
                  0.004970319351166769,
                  0.004249730362908269,
                  0.001757311868472835,
                  0.001448938687579426,
                  0.0011473019737021578,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0.009256945665169677,
                  0.011663768744765874,
                  0.01408719766104635,
                  0.015961133645793116,
                  0.016849206587101546,
                  0.01692610352640172,
                  0.016322854266217185,
                  0.014705610259888176,
                  0.0123775223171112,
                  0.009918670991100529,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0.0021626291558322773,
                  0.0027419380843726293,
                  0.0033501568835823075,
                  0.004930719299214524,
                  0.005495913657669573,
                  0.005850822527472292,
                  0.006004990952831851,
                  0.005800268008262476,
                  0.005279416741803904,
                  0.004620185242937348,
                  0.001869331611896318,
                  0.0015971528094384257,
                  0.0034248819875564067,
                  0.002705541461406362,
                  0.0033093201548148243,
                  0.0038145711263872914,
                  0.004094743138305857,
                  0.004149075222489646,
                  0.0040550735660261385,
                  0.003718823080637759,
                  0.0031789016773076614,
                  0.002572697460581803,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0.0010849269093701403,
                  0.001372336941070821,
                  0.0016693040797700653,
                  0.010658195015974883,
                  0.013087929188189395,
                  0.01547035516945971,
                  0.01729875440111478,
                  0.01807216619683319,
                  0.017923100901379496,
                  0.01712494955879274,
                  0.014408519200525174,
                  0.012197883627417078,
                  0.010939844828081219,
                  0.001420705733640925,
                  0.0017098775414812533,
                  0.0019285398175465712,
                  0.002027399843105309,
                  0.0020324839353620607,
                  0.0019526146674341206,
                  0.0017510549928926446,
                  0.0014682235356433594,
                  0.0011738257954869277,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0.019606502861715395,
                  0.024313848281301672,
                  0.0286005678888702,
                  0.031379387758671426,
                  0.032248214456495346,
                  0.03192734585972676,
                  0.029919577532411843,
                  0.026110363491072756,
                  0.022465626671723436,
                  0.018240626493399387,
                  0.0015964206447289424,
                  0.0018409935502727865,
                  0.0019771306412294937,
                  0.0020038829973326525,
                  0.0019591277745188117,
                  0.0017975347325166844,
                  0.0015372251675769527,
                  0.0034737089910518203,
                  0.0028000851502869776,
                  0.00336327992542448,
                  0.004931233641647252,
                  0.005403607290541217,
                  0.005684869706487335,
                  0.005716492197568957,
                  0.005391721023793164,
                  0.004829990944300036,
                  0.004158189050790314,
                  0.0016674755631389566,
                  0.0013849970696023675,
                  0.0011011706597719004,
                  0,
                  0,
                  0,
                  0,
                  0.004256866559146852,
                  0.005370339501322327,
                  0.006500703209307197,
                  0.008492310621645249,
                  0.009206826050811998,
                  0.009530169875037301,
                  0.009473226833567619,
                  0.008829126734912218,
                  0.0077573284288701225,
                  0.0065291875493307325,
                  0.0016749675082884143,
                  0.0013997164236034109,
                  0.319095306469877,
                  0.39097479998322865,
                  0.4540530607796899,
                  0.4912129162231923
                ],
                "algorithm_manifest": {
                  "name": "core_terrain_scale",
                  "mode": "valley",
                  "window_size": 0.01,
                  "lens_profile": "gravitational"
                }
              },
              "name": "terrain_scale_5_valley",
              "base_frequency": 220.0,
              "notes": [
                {
                  "log_position": 0.011,
                  "frequency": 221.6838272903109,
                  "midi": 57,
                  "cents_from_base": 13.2,
                  "prime_sources": []
                },
                {
                  "log_position": 0.2,
                  "frequency": 252.71363809934772,
                  "midi": 59,
                  "cents_from_base": 240.0,
                  "prime_sources": []
                },
                {
                  "log_position": 0.402,
                  "frequency": 290.6944492448183,
                  "midi": 62,
                  "cents_from_base": 482.40000000000003,
                  "prime_sources": []
                },
                {
                  "log_position": 0.609,
                  "frequency": 335.54436371638246,
                  "midi": 64,
                  "cents_from_base": 730.8,
                  "prime_sources": []
                },
                {
                  "log_position": 0.873,
                  "frequency": 402.9228220239755,
                  "midi": 67,
                  "cents_from_base": 1047.6,
                  "prime_sources": []
                }
              ]
            }
            ```

            `output/terrain_scale_8_valley.json`
            ```json
            {
              "name": "terrain_scale_8_valley",
              "base_frequency": 220.0,
              "notes": [
                {
                  "log_position": 0.0,
                  "frequency": 220.0,
                  "midi": 57,
                  "cents_from_base": 0.0,
                  "prime_sources": []
                },
                {
                  "log_position": 0.07575,
                  "frequency": 231.85993137814998,
                  "midi": 58,
                  "cents_from_base": 90.89999999999999,
                  "prime_sources": []
                },
                {
                  "log_position": 0.178,
                  "frequency": 248.88918182609805,
                  "midi": 59,
                  "cents_from_base": 213.6,
                  "prime_sources": []
                },
                {
                  "log_position": 0.2845,
                  "frequency": 267.9573749645833,
                  "midi": 60,
                  "cents_from_base": 341.4,
                  "prime_sources": []
                },
                {
                  "log_position": 0.495,
                  "frequency": 310.0505661312443,
                  "midi": 63,
                  "cents_from_base": 594.0,
                  "prime_sources": []
                },
                {
                  "log_position": 0.61025,
                  "frequency": 335.8352167377353,
                  "midi": 64,
                  "cents_from_base": 732.3,
                  "prime_sources": []
                },
                {
                  "log_position": 0.672,
                  "frequency": 350.5216423656564,
                  "midi": 65,
                  "cents_from_base": 806.4000000000001,
                  "prime_sources": []
                },
                {
                  "log_position": 0.763,
                  "frequency": 373.3434767505944,
                  "midi": 66,
                  "cents_from_base": 915.6,
                  "prime_sources": []
                },
                {
                  "log_position": 0.95775,
                  "frequency": 427.3012459589087,
                  "midi": 68,
                  "cents_from_base": 1149.3,
                  "prime_sources": []
                },
                {
                  "log_position": 1.0,
                  "frequency": 440.0,
                  "midi": 69,
                  "cents_from_base": 1200.0,
                  "prime_sources": []
                }
              ],
              "log_prime_positions": [
                0.0,
                0.5849625007211562,
                0.32192809488736235,
                0.8073549220576041,
                0.45943161863729726,
                0.7004397181410922,
                0.0874628412503394,
                0.2479275134435855,
                0.5235619560570128,
                0.8579809951275721,
                0.9541963103868752,
                0.20945336562894978,
                0.3575520046180837,
                0.42626475470209796,
                0.5545888516776374,
                0.7279204545631992,
                0.8826430493618412,
                0.9307373375628862,
                0.06608919045777244,
                0.14974711950468206,
                0.18982455888001723,
                0.30378074817710293,
                0.37503943134692475,
                0.47573343096639775,
                0.5999128421871277,
                0.6582114827517948,
                0.6865005271832184,
                0.7414669864011469,
                0.7681843247769263,
                0.8201789624151877,
                0.9886846867721658,
                0.03342300153745028,
                0.09803208296052672,
                0.11894107272350743,
                0.21916852046216156,
                0.2384047393250789,
                0.294620748891627,
                0.34872815423107756,
                0.38370429247405224,
                0.43462822763672465,
                0.4838157772642564,
                0.4998458870832054,
                0.5774288280357487,
                0.5924570372680804,
                0.6220518194563762,
                0.6366246205436489,
                0.7210991887071851,
                0.8008998999203047,
                0.826548487290915,
                0.839203788096944,
                0.8641861446542802,
                0.9008668079807486,
                0.9128893362299616,
                0.971543553950772,
                0.005624549193878107,
                0.03891898929230235,
                0.07146236255662415,
                0.08214904135387156,
                0.11374216604918833,
                0.1344263202209261,
                0.14465824283188233,
                0.19475685442224788,
                0.2620948453701794,
                0.28077077013060253,
                0.2900188469326183,
                0.3083390301394073,
                0.3706874068072177,
                0.3966047811818585,
                0.4387918525782609,
                0.44708322620965224,
                0.4635243732711803,
                0.48784003382305136,
                0.5196362528432128,
                0.5430318202552378,
                0.5660540381710917,
                0.581200581924957,
                0.6036263449861919,
                0.6329951971429578,
                0.6474584264549202,
                0.6759570329417488,
                0.7108064336993516,
                0.7176764230663961,
                0.7515440590890982,
                0.7582232147267249,
                0.7780771295353582,
                0.7911628885550183,
                0.8105716347411469,
                0.8360503550580697,
                0.848622940429338,
                0.8548683832602364,
                0.867278739709662,
                0.9038818457361802,
                0.9277779620823422,
                0.939579214314693,
                0.9628960053372605,
                0.9744145898055271,
                0.9915218460756953,
                0.025139562278508228,
                0.030667136246941375,
                0.07948478382681526,
                0.09539702279255656,
                0.12153351734003176,
                0.13699111208022957,
                0.15228484230658193,
                0.15734693536284278,
                0.17242750864548248,
                0.1972166931100522,
                0.21188829454600366,
                0.22641219278878566,
                0.23122118071118544,
                0.24555270625568207,
                0.2597432636907815,
                0.2691266791494179,
                0.27379559921426466,
                0.301496194982549,
                0.324180546618741,
                0.32867492732794734,
                0.3376219019925075,
                0.3509391815464308,
                0.36413465500805176,
                0.3685064615076917,
                0.3944626946103171,
                0.40301202357499677,
                0.41574176829009046,
                0.4325419003882585,
                0.4532706340106232,
                0.4696418172395161,
                0.4898479604392978,
                0.5058115539195943,
                0.5176693881338119,
                0.5294305541461509,
                0.5372184005385963,
                0.5526690975142717,
                0.5641494899857317,
                0.5717526435035455,
                0.5868397879618266,
                0.5943246039248474,
                0.6202198255074864,
                0.6384359139904717,
                0.6599958924299776,
                0.663558104217273,
                0.6812384117778048,
                0.6847486204216257,
                0.6917435191712747,
                0.6952282914957504,
                0.7125270004398232,
                0.7364019313182902,
                0.7431513941124999,
                0.7465143211384635,
                0.753216749178955,
                0.776433032444733,
                0.7829982089204136,
                0.786269627648466,
                0.7927902943010638,
                0.8249587405285225,
                0.8313072438020508,
                0.8439210512890345,
                0.8595347863826529,
                0.8719052376591868,
                0.8780509127285367,
                0.887220615468385,
                0.896332403909942,
                0.9173720794768412,
                0.9233274854191923,
                0.9322147519683852,
                0.9410476063405806,
                0.9527412471864882,
                0.9614496943981959,
                0.9787104591063572,
                0.9844184588011382,
                0.9929383361658138,
                0.9957671508778014,
                0.009828617368108377,
                0.012624538865059511,
                0.02097993890421177,
                0.0347989625772676,
                0.03754695396217841,
                0.05120894091476479,
                0.053925881531104676,
                0.0620461377204906,
                0.08613622502730917,
                0.09143538632360722,
                0.09407768567190464,
                0.09934781040319289,
                0.10721707559138259,
                0.11504365016170993,
                0.12541347048331486,
                0.13314221240060117,
                0.14082977077300085,
                0.16867211813223043,
                0.17117679765177185,
                0.18363538147321837,
                0.1935253605012151,
                0.20579324939715724,
                0.2131042196419067,
                0.22037832769522803,
                0.2300204357056341,
                0.24436383512051027,
                0.24911345271372837,
                0.25620868852738665,
                0.26326920037266166,
                0.26561504648445733,
                0.2726297849763697,
                0.2865577616079574,
                0.2980625677190165,
                0.3185428097027238,
                0.320800548881637,
                0.3253054550896825,
                0.332036548361651,
                0.3342732853071907,
                0.34096276425169947,
                0.3454052467177954,
                0.3476213685681345,
                0.35204342579543324,
                0.3652288492515447,
                0.36741475124682765,
                0.37395265537019334,
                0.4104513515039947,
                0.41679752760606,
                0.42311591014710065,
                0.4314976042580509,
                0.4501802471647533,
                0.46045589630963657,
                0.4747199465264824,
                0.47876961947576346,
                0.4807902010958165,
                0.48482289426214564,
                0.49085087674029787,
                0.4988492065317246,
                0.5028318040667444,
                0.5048189876328413,
                0.5107641679178909,
                0.5225815312548301,
                0.5323559252888477,
                0.5343028824546305,
                0.5381889320524187,
                0.5401280385820999,
                0.5439984501345413,
                0.5497846679478596,
                0.561287945164829,
                0.5727002264872922,
                0.5802585674997879,
                0.5915223465707349,
                0.5971214287895684,
                0.6008421143873012,
                0.6064052126977847,
                0.6137894644725803,
                0.6174674652941963,
                0.624795455860237,
                0.6284455401371811,
                0.6411485974112326,
                0.644757592516257,
                0.6501542136750937,
                0.6519486107234462,
                0.6555307231556426,
                0.6608872703025659,
                0.6626683755175415,
                0.6679985356725278,
                0.6768386064741535,
                0.6943578872214519,
                0.699572453287269,
                0.7030383889864168,
                0.7047682393625987,
                0.7253662578956417,
                0.7287708495426634,
                0.7304701371842205,
                0.7389366816761394,
                0.7490313820402035,
                0.7507069862249481,
                0.7590559391601697,
                0.7657004876511011,
                0.7706638929167595,
                0.7756102807595381,
                0.780539767471961,
                0.7952279660286782,
                0.8000909876249949,
                0.8033239190414906,
                0.8049376720519082,
                0.814582465906276,
                0.8225708309501679,
                0.8320988460391343,
                0.8384160757973371,
                0.8509681509824382,
                0.8618623400591515,
                0.8665062122262019,
                0.869593843240784,
                0.8711351842430454,
                0.8742129348308743,
                0.8757493514200555,
                0.8834069863883697,
                0.8925428166485521,
                0.8970891283127562,
                0.9016211583461123,
                0.9151324489506503,
                0.9166259222112357,
                0.9285183752578899,
                0.9299980626090264,
                0.9461752407235587,
                0.9505558970475121,
                0.9563761572496702,
                0.960725994839058,
                0.9636186174439726,
                0.9650627567446276,
                0.9679467058127077,
                0.9736973663053519,
                0.9779953686129614,
                0.9851303734668989,
                0.986553149756659,
                0.9936460600165965,
                0.003517912108601999,
                0.01052810588648468,
                0.014717929860009516,
                0.023061249735334684,
                0.024447124040646806,
                0.027214885159835025,
                0.028596777067108246,
                0.0354864512921543,
                0.04371086334715596,
                0.04507705193494059,
                0.05596023445229395,
                0.05731487778270344,
                0.061371192659811016,
                0.06406908038550949,
                0.06541613467654757,
                0.07213260416723374,
                0.07748335685950729,
                0.08945048111590687,
                0.1052537797008831,
                0.10787091427961401,
                0.1117877358010116,
                0.11699367754698069,
                0.12734954105911883,
                0.1286388128525975,
                0.13121390508627231,
                0.13635034145415567,
                0.1465686757407859,
                0.14784089367233738,
                0.1503819688178478,
                0.15545073131213738,
                0.15924065041167257,
                0.1630206395807935,
                0.16553514137792383,
                0.1730524577741152,
                0.17430154446763094,
                0.18797059198419924,
                0.19167614635242758,
                0.19290921911201275,
                0.19660212652317027,
                0.19905882365302136,
                0.20273604325016747,
                0.21127994748200787,
                0.2149261879424347,
                0.21735190527033407,
                0.21856323619027096,
                0.22219113845633223,
                0.2246046815384989,
                0.22821744229343455,
                0.23541593560252613,
                0.23900175776558263,
                0.24257868945134645,
                0.2508905357233407,
                0.2532565797811539,
                0.25679838607938965,
                0.26385601959608235,
                0.2685420003001231,
                0.2720465243899378,
                0.27437815324636305,
                0.28944257568833187,
                0.2997804028585398,
                0.3054917921106841,
                0.3100446796475057,
                0.31231574669010626,
                0.31571565802220175,
                0.31684718360247227,
                0.32023644524164885,
                0.3325960577892141,
                0.33929330018009435,
                0.3404064908532946,
                0.3492812288174521,
                0.3536982090480348,
                0.3559016383284175,
                0.36249180604606285,
                0.3701424794953985,
                0.3755825124905066,
                0.37666806185766766,
                0.3788367132106142,
                0.3831642606351099,
                0.3864014236407778,
                0.3896313392605211,
                0.39178060601316606,
                0.39285403987287304,
                0.39499851450167184,
                0.3982092614668516,
                0.4024791722149637,
                0.4046093978377117,
                0.40567333228186614,
                0.40886043602476,
                0.41415667927414057,
                0.41521359876528635,
                0.42048661282577515,
                0.42469119151295326,
                0.4267888945955612,
                0.43410692860995465,
                0.43931146181884595,
                0.4455322190283121,
                0.4465664090660673,
                0.4496645384761917,
                0.4517262680745064,
                0.4527560290324939,
                0.46096776257042177,
                0.46811488637809856,
                0.4701504352743589,
                0.4731983836775274,
                0.4772523239379527,
                0.48028532093637194,
                0.48230378232318294,
                0.4913520735634345,
                0.4953553922359819,
                0.5003439692704034,
                0.5033288566266617,
                0.5063075811003064,
                0.5102696708981777,
                0.5152070304087505,
                0.5211096436513325,
                0.5279656411339543,
                0.5299185281203243,
                0.5328429109612823,
                0.5357613779866555,
                0.5367328898354145,
                0.5502658068687403,
                0.5512276035982883,
                0.5560269927246775,
                0.5598550415136251,
                0.5617652636277072,
                0.5684311931674597,
                0.5703301010307977,
                0.5741204350097483,
                0.5797873295269915,
                0.5826124512670195,
                0.5882461520448172,
                0.5901191741071752,
                0.5929241556276377,
                0.602234901341064,
                0.606867837374152,
                0.6077926419192102,
                0.6151698138436029,
                0.6270778405173937,
                0.62890115202819,
                0.6298119443822336,
                0.6352646565395134,
                0.6379833037778532,
                0.639792893279312,
                0.6452080827746836,
                0.6479080742818075,
                0.6515002206527385,
                0.6532929453828148,
                0.6568717256139808,
                0.6666678406903559,
                0.6675551070411319,
                0.6693280043959033,
                0.6702136367385642,
                0.6755160440827783,
                0.6878130625649308,
                0.688687423222536,
                0.6913073301911148,
                0.6939224880810145,
                0.6965329140782999,
                0.6982705776920315,
                0.7008731551402632,
                0.7017396386743512,
                0.7069276396174033,
                0.7086528356865296,
                0.7138160802344985,
                0.7146748273080018,
                0.7189609119842102,
                0.7198166030181266,
                0.7266439214839944,
                0.7274950690254308,
                0.7342862320963465,
                0.7368246990988654,
                0.7452541419572566,
                0.7519624134608536,
                0.7553048882623986,
                0.7569732261654476,
                0.7578066721972284,
                0.7594721212028334,
                0.7603041252863822,
                0.7694246415527535,
                0.7727269492398494,
                0.7776662808807551,
                0.7801296196253069,
                0.7842258604262518,
                0.7850437147797241,
                0.7866780338906524,
                0.7891260464252304,
                0.7899411283909162,
                0.7923836149351887,
                0.7964452590618504,
                0.7972562175097855,
                0.8021124185860656,
                0.8061468033205245,
                0.8069523282107361,
                0.8109732200021641,
                0.8165837077875703,
                0.8189815394324435,
                0.8205778826557742,
                0.8229690904532875,
                0.8261512148002071,
                0.8285332104556169,
                0.8309112797427821,
                0.8372337003390872,
                0.8419573990995474,
                0.8427431807316577,
                0.8443134612032963,
                0.8497960222456086,
                0.8521393281872431,
                0.8536994203002205,
                0.8568145525030096,
                0.8606990326119877,
                0.8637991037288498,
                0.8661197933030698,
                0.8684367558581688,
                0.8769005910403064,
                0.8792003179473926,
                0.8799660796643566,
                0.8837888032599616,
                0.8891236562942374,
                0.8906442836190891,
                0.8929222236305911,
                0.8997345423575112,
                0.9004894848346487,
                0.9042582828005179,
                0.9095181142966149,
                0.9110174077969856,
                0.91176647065955,
                0.9155059622319313,
                0.9207250197511805,
                0.9222127177854481,
                0.9251835194342084,
                0.931845540183673,
                0.9333218207329452,
                0.9355334129507464,
                0.9362698576022096,
                0.9377416200770955,
                0.9399464524586867,
                0.940680648424094,
                0.9450779951078164,
                0.9465408038931034,
                0.9538326821452806,
                0.9618114080871633,
                0.9661449133456019,
                0.9668659003875385,
                0.9683067944307979,
                0.9704654407799953,
                0.9726208620587452,
                0.9733386208003605,
                0.9754897569457541,
                0.9833499276764576,
                0.9840623696864367,
                0.9861975872062728,
                0.9918760990034149,
                0.9939997917925231,
                0.9982378218880463,
                0.9989429514430849,
                0.0010562746347787082,
                0.005273656563937457,
                0.01087772300703463,
                0.011576703176177101,
                0.012973648374540184,
                0.015066533230290653,
                0.019938156424795017,
                0.021327032624372442,
                0.02202096964635623,
                0.02825142816279274,
                0.03651707048651743,
                0.03994716016909401,
                0.04200130627913355,
                0.042685372219350995,
                0.0461008450288017,
                0.04678297035635037,
                0.05018876759643462,
                0.05086896329073618,
                0.054265139625763625,
                0.0562990145503375,
                0.0569763361782193,
                0.060358182642141746,
                0.06103360168111159,
                0.06440596189104232,
                0.06642560063555628,
                0.06911406177393854,
                0.07915140542189122,
                0.082481727863103,
                0.0831468708167424,
                0.08646799346406825,
                0.08911939791516776,
                0.0911047583764998,
                0.09440763308120761,
                0.10033381912654146,
                0.1023038172126472,
                0.1062357616157476,
                0.11015701895406627,
                0.11080952689865343,
                0.11666885596711275,
                0.11861668935150811,
                0.11991378545226924,
                0.12185724561265432,
                0.1237980912518551,
                0.1296050111525053,
                0.13024878405068832,
                0.1334633465234383,
                0.1379517347153589,
                0.13987106321248732,
                0.141149198437516,
                0.14178784167100345,
                0.14306428063141116,
                0.15069928874453978,
                0.1513337192916543,
                0.15513445485775462,
                0.15703107437835415,
                0.1620765703743126,
                0.16459271671236608,
                0.16647695081680386,
                0.16835872722388634,
                0.17398937416653434,
                0.1789760113745256,
                0.179598130849836,
                0.18084156556666162,
                0.18270471051896423,
                0.18332522452461136,
                0.185185166820328,
                0.18704271433989453,
                0.19013332186479961,
                0.19198451336031078,
                0.1956797854959813,
                0.19936561685798163,
                0.2048767676039932,
                0.20548782015056521,
                0.20731942645780443,
                0.2085392067383636,
                0.21401549141084386,
                0.2164427391604921,
                0.22370007598630548,
                0.22490609071976633,
                0.2255087202360011,
                0.22671322461896268,
                0.2285180977161938,
                0.22911922065859433,
                0.23272070796487232,
                0.23391920858697732,
                0.2381061374320769,
                0.24703741878858157,
                0.2500022678404482,
                0.25177825703586765,
                0.2553236900081373,
                0.2594490462856853,
                0.2612134513660483,
                0.2641493397233282,
                0.267664537501119,
                0.2682495719944925,
                0.2694189297410967,
                0.27117119113977284,
                0.2735042339621607,
                0.2752515434703267,
                0.27815903143723814,
                0.2787398265501099,
                0.27990071580276177,
                0.2839564876651143,
                0.2856911913300926,
                0.287423811683523,
                0.2885777369927027,
                0.2903068962579017,
                0.2908828224295776,
                0.2937590096678642,
                0.29433355967182945,
                0.2989217409697527,
                0.3023533264312026,
                0.30463652380727074,
                0.30976054472962244,
                0.3108967487977128,
                0.3125993788626288,
                0.3159986226285593,
                0.3165643853969428,
                0.3182603437124159,
                0.3199543106869433,
                0.3216462909913811,
                0.3295160672065345,
                0.3311968771530289,
                0.33511116842486033,
                0.33622758948338893,
                0.3384578431308483,
                0.34124082053874866,
                0.3434633436679025,
                0.34679072175070236,
                0.3517674439598926,
                0.3528710546779962,
                0.35342254361471515,
                0.354524889449351,
                0.3611213347347894,
                0.36440828137983244,
                0.3660489506706283,
                0.36659542607143847,
                0.37095979329738565,
                0.3725930331407459,
                0.37422442612373114,
                0.37802385092548596,
                0.38073161268299416,
                0.3845139613986182,
                0.38559281360136244,
                0.39365859145477394,
                0.39526634983909553,
                0.39687231851056004,
                0.3984765014492567,
                0.4006126410819993,
                0.40221267271464206,
                0.40327837547105266,
                0.4038109317860291,
                0.40700214792420075,
                0.4085951127981016,
                0.4096561130598506,
                0.4101863207250939,
                0.4117757755765272,
                0.41758884038257976,
                0.41917016502853727,
                0.41969688830597957,
                0.4207497582967991,
                0.42547818764532785,
                0.4260026133293609,
                0.42705089315087835,
                0.43019117019169584,
                0.43071388579193914,
                0.432280897214161,
                0.4333246267159252,
                0.4400905249504887,
                0.44164739025361266,
                0.44320257729701173,
                0.4442384380781054,
                0.4463079310503461,
                0.448890629629262,
                0.457124331540804,
                0.4612236276133712,
                0.4617352216048631,
                0.46326891598128944,
                0.4642904738507662,
                0.4648009816554169,
                0.4658214556437746,
                0.4663314220827675,
                0.4688785538194264,
                0.4724370000513295,
                0.47395936569476105,
                0.4749733843911463,
                0.4769992861330614,
                0.47952766925634743,
                0.4810425749337537,
                0.4860808026519688,
                0.48708634027127024,
                0.4875888463860298,
                0.48909531541350365,
                0.4966041545756027,
                0.4976023867834886,
                0.49959678148975406,
                0.5020859039859038,
                0.5035773187026894,
                0.505067193231886,
                0.5070513022479163,
                0.5085375953473218,
                0.511505595792482,
                0.5124935739450386,
                0.5139742737406572,
                0.5144675028192696,
                0.5159461791095175,
                0.5169311219986964,
                0.518407276671365,
                0.5188989927773142,
                0.5213550625582591,
                0.521845775161932,
                0.5257654788219156,
                0.5272326264475666,
                0.5321123707949986,
                0.5330863421676119,
                0.5360043172885496,
                0.5394011790281124,
                0.5461710022673503,
                0.5476175549028021,
                0.5524289485264698,
                0.5533893047216185,
                0.5577030140377671,
                0.5596160858127246,
                0.5610492266996714,
                0.562003863651552,
                0.5634346357101978,
                0.5667675960329165,
                0.568193653850073,
                0.5696183034466413,
                0.5719895976045772,
                0.5724633890836759,
                0.5748300153376306,
                0.5776648517648459,
                0.579551652806564,
                0.5819066893087674,
                0.5823772356406912,
                0.584727667963921,
                0.5866052606036105,
                0.5894170757686097,
                0.59175607602299,
                0.5973542529716099,
                0.5978197886455071,
                0.5987504095717541,
                0.6006098524467063,
                0.6020028635374455,
                0.6029307909152394,
                0.6047848570864205,
                0.6089478145655136,
                0.6112553886993383,
                0.6126381636047704,
                0.6140196144357212,
                0.6144798042453293,
                0.6158594935830806,
                0.6181560477784586,
                0.6209070958853374,
                0.621365094314863,
                0.6236529080529251,
                0.6250238568804067,
                0.6263935041739958,
                0.6277618524026157,
                0.6295843001938498,
                0.6309496268328699,
                0.6332223038007883,
                0.6345841934936988,
                0.6350378711832515,
                0.6363980488838367,
                0.6377569454121438,
                0.6391145631794136,
                0.6413744242945126,
                0.6431797679255485,
                0.6485822833637354,
                0.6499297570366186,
                0.6548597542073936,
                0.6553071015104783,
                0.6593269974141057,
                0.6602187885356182,
                0.6620007187184807,
                0.6642250408379288,
                0.6708775043969794,
                0.6726463261246257,
                0.6766182635885187,
                0.677499433285107,
                0.6779398163901409,
                0.6801397177631712,
                0.6814580502102743,
                0.6818972267862347,
                0.6832139549344266,
                0.684091106529095,
                0.6880317024139343,
                0.6897796293772747,
                0.6923975554684855,
                0.6963155588928207,
                0.6997893183821364,
                0.7010898248171574,
                0.701523066574434,
                0.7041197885130172,
                0.7054163988826986,
                0.7075748299269733,
                0.7080061288960716,
                0.7101606917829137,
                0.710591218506756,
                0.7118820283520872,
                0.7140308149287833,
                0.7170337494908909,
                0.7178905839872806,
                0.7230209318120316,
                0.7234476384229178,
                0.7268567554507281,
                0.7272823292121885,
                0.7294083169840191,
                0.7298331388483634,
                0.7319553737719341,
                0.7361905009609265,
                0.7370360365402291,
                0.7374586185704587,
                0.7383034114746381,
                0.7399915146842255,
                0.7433618068658647,
                0.7446236393435842,
                0.7458843691420391,
                0.7463043677013049,
                0.748821794614704,
                0.7521715451624431,
                0.7538435083116375,
                0.7546787638225287,
                0.7559307410843987,
                0.7621743819931017,
                0.7625896655425694,
                0.7646642920733461,
                0.7650788596166841,
                0.7663218479539611,
                0.7671499122848527,
                0.768391118304248,
                0.7696312573842401,
                0.7712831196410048,
                0.7725207763147556,
                0.7733452912912706,
                0.7758160126730259,
                0.7770497884388311,
                0.7786931832238406,
                0.7811547706958628,
                0.7819743673893382,
                0.7848392946531492,
                0.7872904265595811,
                0.7893298600924323,
                0.7942127699830656,
                0.7954309195411307,
                0.797864137333749,
                0.7990792090290064,
                0.7994840056200149,
                0.803929287974447,
                0.8055423643587234,
                0.8091652053718806,
                0.8111739707213205,
                0.8123778887668927,
                0.81518313000803,
                0.8159836266527256,
                0.8163837084747264,
                0.8175832886776159,
                0.8195803751550043,
                0.8211760562698536,
                0.8223716599633273,
                0.823168178984741,
                0.8243621335694837,
                0.8303171298102074,
                0.8330877384220085,
                0.8350634920050951,
                0.835458318236593,
                0.8378250091966943,
                0.839794290202557,
                0.8401878240404824,
                0.8433322362175774,
                0.843724806299153,
                0.8472531383208399,
                0.8519441979994987,
                0.8554525097440467,
                0.8566200536768453,
                0.8597288926783899,
                0.8632183475824409,
                0.8643796261862391,
                0.8647665114234434,
                0.8682438177046363,
                0.8690154155520912,
                0.8701720391102115,
                0.8705573743264149,
                0.8724825081067245,
                0.8740207676589766,
                0.8759412884975539,
                0.8770923750274136,
                0.87824254386927,
                0.8797746773369265,
                0.8805401343337341,
                0.8816875588700049,
                0.8820698310081421,
                0.8839796738087469,
                0.8843613391657054,
                0.8866492133719767,
                0.8874110325531844,
                0.8885530075792138,
                0.889694079382086,
                0.8900742361803039,
                0.8923530757341089,
                0.8931118897113073,
                0.8957646000163985,
                0.8991680761343226,
                0.8999233150160584,
                0.9010554325532718,
                0.9048227542942096,
                0.905575039562664,
                0.907078434296485,
                0.9082049531258904,
                0.9089554772894621,
                0.9104553553098212,
                0.9112047099771758,
                0.9138243904080626,
                0.9149456560403241,
                0.915692682615404,
                0.9183042336999331,
                0.9205389495837866,
                0.9212830863073839,
                0.9216550107850531,
                0.9272224027246435,
                0.9279631010034675,
                0.9323993224337926,
                0.9335062496294431,
                0.9346123281713974,
                0.9368219444923792,
                0.9390281817632533,
                0.9415978682660954,
                0.942697762886757,
                0.9434305603835986,
                0.9437968195987897,
                0.9445290591987692,
                0.9478195460200277,
                0.9489147093121594,
                0.9511025450013421
              ],
              "segment_boundaries": [
                0.0,
                0.125,
                0.25,
                0.375,
                0.5,
                0.625,
                0.75,
                0.875,
                1.0
              ]
            }
            ```

            `output/terrain_scale_{num_notes}_{mode}.json`
            ```json
            {
              "metadata": {
                "primes": [
                  2,
                  3,
                  5,
                  7,
                  11,
                  13,
                  17,
                  19,
                  23,
                  29,
                  31,
                  37,
                  41,
                  43,
                  47,
                  53,
                  59,
                  61,
                  67,
                  71,
                  73,
                  79,
                  83,
                  89,
                  97,
                  101,
                  103,
                  107,
                  109,
                  113,
                  127,
                  131,
                  137,
                  139,
                  149,
                  151,
                  157,
                  163,
                  167,
                  173,
                  179,
                  181,
                  191,
                  193,
                  197,
                  199,
                  211,
                  223,
                  227,
                  229,
                  233,
                  239,
                  241,
                  251,
                  257,
                  263,
                  269,
                  271,
                  277,
                  281,
                  283,
                  293,
                  307,
                  311,
                  313,
                  317,
                  331,
                  337,
                  347,
                  349,
                  353,
                  359,
                  367,
                  373,
                  379,
                  383,
                  389,
                  397,
                  401,
                  409,
                  419,
                  421,
                  431,
                  433,
                  439,
                  443,
                  449,
                  457,
                  461,
                  463,
                  467,
                  479,
                  487,
                  491,
                  499,
                  503,
                  509,
                  521,
                  523,
                  541
                ],
                "prime_count": 100,
                "linear_prime_positions": [
                  1.0,
                  1.5,
                  1.25,
                  1.75,
                  1.375,
                  1.625,
                  1.0625,
                  1.1875,
                  1.4375,
                  1.8125,
                  1.9375,
                  1.15625,
                  1.28125,
                  1.34375,
                  1.46875,
                  1.65625,
                  1.84375,
                  1.90625,
                  1.046875,
                  1.109375,
                  1.140625,
                  1.234375,
                  1.296875,
                  1.390625,
                  1.515625,
                  1.578125,
                  1.609375,
                  1.671875,
                  1.703125,
                  1.765625,
                  1.984375,
                  1.0234375,
                  1.0703125,
                  1.0859375,
                  1.1640625,
                  1.1796875,
                  1.2265625,
                  1.2734375,
                  1.3046875,
                  1.3515625,
                  1.3984375,
                  1.4140625,
                  1.4921875,
                  1.5078125,
                  1.5390625,
                  1.5546875,
                  1.6484375,
                  1.7421875,
                  1.7734375,
                  1.7890625,
                  1.8203125,
                  1.8671875,
                  1.8828125,
                  1.9609375,
                  1.00390625,
                  1.02734375,
                  1.05078125,
                  1.05859375,
                  1.08203125,
                  1.09765625,
                  1.10546875,
                  1.14453125,
                  1.19921875,
                  1.21484375,
                  1.22265625,
                  1.23828125,
                  1.29296875,
                  1.31640625,
                  1.35546875,
                  1.36328125,
                  1.37890625,
                  1.40234375,
                  1.43359375,
                  1.45703125,
                  1.48046875,
                  1.49609375,
                  1.51953125,
                  1.55078125,
                  1.56640625,
                  1.59765625,
                  1.63671875,
                  1.64453125,
                  1.68359375,
                  1.69140625,
                  1.71484375,
                  1.73046875,
                  1.75390625,
                  1.78515625,
                  1.80078125,
                  1.80859375,
                  1.82421875,
                  1.87109375,
                  1.90234375,
                  1.91796875,
                  1.94921875,
                  1.96484375,
                  1.98828125,
                  1.017578125,
                  1.021484375,
                  1.056640625
                ],
                "log_prime_positions": [
                  0.0,
                  0.5849625007211562,
                  0.32192809488736235,
                  0.8073549220576041,
                  0.45943161863729726,
                  0.7004397181410922,
                  0.0874628412503394,
                  0.2479275134435855,
                  0.5235619560570128,
                  0.8579809951275721,
                  0.9541963103868752,
                  0.20945336562894978,
                  0.3575520046180837,
                  0.42626475470209796,
                  0.5545888516776374,
                  0.7279204545631992,
                  0.8826430493618412,
                  0.9307373375628862,
                  0.06608919045777244,
                  0.14974711950468206,
                  0.18982455888001723,
                  0.30378074817710293,
                  0.37503943134692475,
                  0.47573343096639775,
                  0.5999128421871277,
                  0.6582114827517948,
                  0.6865005271832184,
                  0.7414669864011469,
                  0.7681843247769263,
                  0.8201789624151877,
                  0.9886846867721658,
                  0.03342300153745028,
                  0.09803208296052672,
                  0.11894107272350743,
                  0.21916852046216156,
                  0.2384047393250789,
                  0.294620748891627,
                  0.34872815423107756,
                  0.38370429247405224,
                  0.43462822763672465,
                  0.4838157772642564,
                  0.4998458870832054,
                  0.5774288280357487,
                  0.5924570372680804,
                  0.6220518194563762,
                  0.6366246205436489,
                  0.7210991887071851,
                  0.8008998999203047,
                  0.826548487290915,
                  0.839203788096944,
                  0.8641861446542802,
                  0.9008668079807486,
                  0.9128893362299616,
                  0.971543553950772,
                  0.005624549193878107,
                  0.03891898929230235,
                  0.07146236255662415,
                  0.08214904135387156,
                  0.11374216604918833,
                  0.1344263202209261,
                  0.14465824283188233,
                  0.19475685442224788,
                  0.2620948453701794,
                  0.28077077013060253,
                  0.2900188469326183,
                  0.3083390301394073,
                  0.3706874068072177,
                  0.3966047811818585,
                  0.4387918525782609,
                  0.44708322620965224,
                  0.4635243732711803,
                  0.48784003382305136,
                  0.5196362528432128,
                  0.5430318202552378,
                  0.5660540381710917,
                  0.581200581924957,
                  0.6036263449861919,
                  0.6329951971429578,
                  0.6474584264549202,
                  0.6759570329417488,
                  0.7108064336993516,
                  0.7176764230663961,
                  0.7515440590890982,
                  0.7582232147267249,
                  0.7780771295353582,
                  0.7911628885550183,
                  0.8105716347411469,
                  0.8360503550580697,
                  0.848622940429338,
                  0.8548683832602364,
                  0.867278739709662,
                  0.9038818457361802,
                  0.9277779620823422,
                  0.939579214314693,
                  0.9628960053372605,
                  0.9744145898055271,
                  0.9915218460756953,
                  0.025139562278508228,
                  0.030667136246941375,
                  0.07948478382681526
                ],
                "x_axis": [
                  0.0,
                  0.001,
                  0.002,
                  0.003,
                  0.004,
                  0.005,
                  0.006,
                  0.007,
                  0.008,
                  0.009,
                  0.01,
                  0.011,
                  0.012,
                  0.013,
                  0.014,
                  0.015,
                  0.016,
                  0.017,
                  0.018,
                  0.019,
                  0.02,
                  0.021,
                  0.022,
                  0.023,
                  0.024,
                  0.025,
                  0.026,
                  0.027,
                  0.028,
                  0.029,
                  0.03,
                  0.031,
                  0.032,
                  0.033,
                  0.034,
                  0.035,
                  0.036,
                  0.037,
                  0.038,
                  0.039,
                  0.04,
                  0.041,
                  0.042,
                  0.043,
                  0.044,
                  0.045,
                  0.046,
                  0.047,
                  0.048,
                  0.049,
                  0.05,
                  0.051,
                  0.052,
                  0.053,
                  0.054,
                  0.055,
                  0.056,
                  0.057,
                  0.058,
                  0.059,
                  0.06,
                  0.061,
                  0.062,
                  0.063,
                  0.064,
                  0.065,
                  0.066,
                  0.067,
                  0.068,
                  0.069,
                  0.07,
                  0.071,
                  0.072,
                  0.073,
                  0.074,
                  0.075,
                  0.076,
                  0.077,
                  0.078,
                  0.079,
                  0.08,
                  0.081,
                  0.082,
                  0.083,
                  0.084,
                  0.085,
                  0.086,
                  0.087,
                  0.088,
                  0.089,
                  0.09,
                  0.091,
                  0.092,
                  0.093,
                  0.094,
                  0.095,
                  0.096,
                  0.097,
                  0.098,
                  0.099,
                  0.1,
                  0.101,
                  0.102,
                  0.103,
                  0.104,
                  0.105,
                  0.106,
                  0.107,
                  0.108,
                  0.109,
                  0.11,
                  0.111,
                  0.112,
                  0.113,
                  0.114,
                  0.115,
                  0.116,
                  0.117,
                  0.118,
                  0.119,
                  0.12,
                  0.121,
                  0.122,
                  0.123,
                  0.124,
                  0.125,
                  0.126,
                  0.127,
                  0.128,
                  0.129,
                  0.13,
                  0.131,
                  0.132,
                  0.133,
                  0.134,
                  0.135,
                  0.136,
                  0.137,
                  0.138,
                  0.139,
                  0.14,
                  0.141,
                  0.142,
                  0.143,
                  0.144,
                  0.145,
                  0.146,
                  0.147,
                  0.148,
                  0.149,
                  0.15,
                  0.151,
                  0.152,
                  0.153,
                  0.154,
                  0.155,
                  0.156,
                  0.157,
                  0.158,
                  0.159,
                  0.16,
                  0.161,
                  0.162,
                  0.163,
                  0.164,
                  0.165,
                  0.166,
                  0.167,
                  0.168,
                  0.169,
                  0.17,
                  0.171,
                  0.172,
                  0.173,
                  0.174,
                  0.175,
                  0.176,
                  0.177,
                  0.178,
                  0.179,
                  0.18,
                  0.181,
                  0.182,
                  0.183,
                  0.184,
                  0.185,
                  0.186,
                  0.187,
                  0.188,
                  0.189,
                  0.19,
                  0.191,
                  0.192,
                  0.193,
                  0.194,
                  0.195,
                  0.196,
                  0.197,
                  0.198,
                  0.199,
                  0.2,
                  0.201,
                  0.202,
                  0.203,
                  0.204,
                  0.205,
                  0.206,
                  0.207,
                  0.208,
                  0.209,
                  0.21,
                  0.211,
                  0.212,
                  0.213,
                  0.214,
                  0.215,
                  0.216,
                  0.217,
                  0.218,
                  0.219,
                  0.22,
                  0.221,
                  0.222,
                  0.223,
                  0.224,
                  0.225,
                  0.226,
                  0.227,
                  0.228,
                  0.229,
                  0.23,
                  0.231,
                  0.232,
                  0.233,
                  0.234,
                  0.235,
                  0.236,
                  0.237,
                  0.238,
                  0.239,
                  0.24,
                  0.241,
                  0.242,
                  0.243,
                  0.244,
                  0.245,
                  0.246,
                  0.247,
                  0.248,
                  0.249,
                  0.25,
                  0.251,
                  0.252,
                  0.253,
                  0.254,
                  0.255,
                  0.256,
                  0.257,
                  0.258,
                  0.259,
                  0.26,
                  0.261,
                  0.262,
                  0.263,
                  0.264,
                  0.265,
                  0.266,
                  0.267,
                  0.268,
                  0.269,
                  0.27,
                  0.271,
                  0.272,
                  0.273,
                  0.274,
                  0.275,
                  0.276,
                  0.277,
                  0.278,
                  0.279,
                  0.28,
                  0.281,
                  0.282,
                  0.283,
                  0.284,
                  0.285,
                  0.286,
                  0.287,
                  0.288,
                  0.289,
                  0.29,
                  0.291,
                  0.292,
                  0.293,
                  0.294,
                  0.295,
                  0.296,
                  0.297,
                  0.298,
                  0.299,
                  0.3,
                  0.301,
                  0.302,
                  0.303,
                  0.304,
                  0.305,
                  0.306,
                  0.307,
                  0.308,
                  0.309,
                  0.31,
                  0.311,
                  0.312,
                  0.313,
                  0.314,
                  0.315,
                  0.316,
                  0.317,
                  0.318,
                  0.319,
                  0.32,
                  0.321,
                  0.322,
                  0.323,
                  0.324,
                  0.325,
                  0.326,
                  0.327,
                  0.328,
                  0.329,
                  0.33,
                  0.331,
                  0.332,
                  0.333,
                  0.334,
                  0.335,
                  0.336,
                  0.337,
                  0.338,
                  0.339,
                  0.34,
                  0.341,
                  0.342,
                  0.343,
                  0.344,
                  0.345,
                  0.346,
                  0.347,
                  0.348,
                  0.349,
                  0.35,
                  0.351,
                  0.352,
                  0.353,
                  0.354,
                  0.355,
                  0.356,
                  0.357,
                  0.358,
                  0.359,
                  0.36,
                  0.361,
                  0.362,
                  0.363,
                  0.364,
                  0.365,
                  0.366,
                  0.367,
                  0.368,
                  0.369,
                  0.37,
                  0.371,
                  0.372,
                  0.373,
                  0.374,
                  0.375,
                  0.376,
                  0.377,
                  0.378,
                  0.379,
                  0.38,
                  0.381,
                  0.382,
                  0.383,
                  0.384,
                  0.385,
                  0.386,
                  0.387,
                  0.388,
                  0.389,
                  0.39,
                  0.391,
                  0.392,
                  0.393,
                  0.394,
                  0.395,
                  0.396,
                  0.397,
                  0.398,
                  0.399,
                  0.4,
                  0.401,
                  0.402,
                  0.403,
                  0.404,
                  0.405,
                  0.406,
                  0.407,
                  0.408,
                  0.409,
                  0.41,
                  0.411,
                  0.412,
                  0.413,
                  0.414,
                  0.415,
                  0.416,
                  0.417,
                  0.418,
                  0.419,
                  0.42,
                  0.421,
                  0.422,
                  0.423,
                  0.424,
                  0.425,
                  0.426,
                  0.427,
                  0.428,
                  0.429,
                  0.43,
                  0.431,
                  0.432,
                  0.433,
                  0.434,
                  0.435,
                  0.436,
                  0.437,
                  0.438,
                  0.439,
                  0.44,
                  0.441,
                  0.442,
                  0.443,
                  0.444,
                  0.445,
                  0.446,
                  0.447,
                  0.448,
                  0.449,
                  0.45,
                  0.451,
                  0.452,
                  0.453,
                  0.454,
                  0.455,
                  0.456,
                  0.457,
                  0.458,
                  0.459,
                  0.46,
                  0.461,
                  0.462,
                  0.463,
                  0.464,
                  0.465,
                  0.466,
                  0.467,
                  0.468,
                  0.469,
                  0.47,
                  0.471,
                  0.472,
                  0.473,
                  0.474,
                  0.475,
                  0.476,
                  0.477,
                  0.478,
                  0.479,
                  0.48,
                  0.481,
                  0.482,
                  0.483,
                  0.484,
                  0.485,
                  0.486,
                  0.487,
                  0.488,
                  0.489,
                  0.49,
                  0.491,
                  0.492,
                  0.493,
                  0.494,
                  0.495,
                  0.496,
                  0.497,
                  0.498,
                  0.499,
                  0.5,
                  0.501,
                  0.502,
                  0.503,
                  0.504,
                  0.505,
                  0.506,
                  0.507,
                  0.508,
                  0.509,
                  0.51,
                  0.511,
                  0.512,
                  0.513,
                  0.514,
                  0.515,
                  0.516,
                  0.517,
                  0.518,
                  0.519,
                  0.52,
                  0.521,
                  0.522,
                  0.523,
                  0.524,
                  0.525,
                  0.526,
                  0.527,
                  0.528,
                  0.529,
                  0.53,
                  0.531,
                  0.532,
                  0.533,
                  0.534,
                  0.535,
                  0.536,
                  0.537,
                  0.538,
                  0.539,
                  0.54,
                  0.541,
                  0.542,
                  0.543,
                  0.544,
                  0.545,
                  0.546,
                  0.547,
                  0.548,
                  0.549,
                  0.55,
                  0.551,
                  0.552,
                  0.553,
                  0.554,
                  0.555,
                  0.556,
                  0.557,
                  0.558,
                  0.559,
                  0.56,
                  0.561,
                  0.562,
                  0.563,
                  0.564,
                  0.565,
                  0.566,
                  0.567,
                  0.568,
                  0.569,
                  0.57,
                  0.571,
                  0.572,
                  0.573,
                  0.574,
                  0.575,
                  0.576,
                  0.577,
                  0.578,
                  0.579,
                  0.58,
                  0.581,
                  0.582,
                  0.583,
                  0.584,
                  0.585,
                  0.586,
                  0.587,
                  0.588,
                  0.589,
                  0.59,
                  0.591,
                  0.592,
                  0.593,
                  0.594,
                  0.595,
                  0.596,
                  0.597,
                  0.598,
                  0.599,
                  0.6,
                  0.601,
                  0.602,
                  0.603,
                  0.604,
                  0.605,
                  0.606,
                  0.607,
                  0.608,
                  0.609,
                  0.61,
                  0.611,
                  0.612,
                  0.613,
                  0.614,
                  0.615,
                  0.616,
                  0.617,
                  0.618,
                  0.619,
                  0.62,
                  0.621,
                  0.622,
                  0.623,
                  0.624,
                  0.625,
                  0.626,
                  0.627,
                  0.628,
                  0.629,
                  0.63,
                  0.631,
                  0.632,
                  0.633,
                  0.634,
                  0.635,
                  0.636,
                  0.637,
                  0.638,
                  0.639,
                  0.64,
                  0.641,
                  0.642,
                  0.643,
                  0.644,
                  0.645,
                  0.646,
                  0.647,
                  0.648,
                  0.649,
                  0.65,
                  0.651,
                  0.652,
                  0.653,
                  0.654,
                  0.655,
                  0.656,
                  0.657,
                  0.658,
                  0.659,
                  0.66,
                  0.661,
                  0.662,
                  0.663,
                  0.664,
                  0.665,
                  0.666,
                  0.667,
                  0.668,
                  0.669,
                  0.67,
                  0.671,
                  0.672,
                  0.673,
                  0.674,
                  0.675,
                  0.676,
                  0.677,
                  0.678,
                  0.679,
                  0.68,
                  0.681,
                  0.682,
                  0.683,
                  0.684,
                  0.685,
                  0.686,
                  0.687,
                  0.688,
                  0.689,
                  0.69,
                  0.691,
                  0.692,
                  0.693,
                  0.694,
                  0.695,
                  0.696,
                  0.697,
                  0.698,
                  0.699,
                  0.7,
                  0.701,
                  0.702,
                  0.703,
                  0.704,
                  0.705,
                  0.706,
                  0.707,
                  0.708,
                  0.709,
                  0.71,
                  0.711,
                  0.712,
                  0.713,
                  0.714,
                  0.715,
                  0.716,
                  0.717,
                  0.718,
                  0.719,
                  0.72,
                  0.721,
                  0.722,
                  0.723,
                  0.724,
                  0.725,
                  0.726,
                  0.727,
                  0.728,
                  0.729,
                  0.73,
                  0.731,
                  0.732,
                  0.733,
                  0.734,
                  0.735,
                  0.736,
                  0.737,
                  0.738,
                  0.739,
                  0.74,
                  0.741,
                  0.742,
                  0.743,
                  0.744,
                  0.745,
                  0.746,
                  0.747,
                  0.748,
                  0.749,
                  0.75,
                  0.751,
                  0.752,
                  0.753,
                  0.754,
                  0.755,
                  0.756,
                  0.757,
                  0.758,
                  0.759,
                  0.76,
                  0.761,
                  0.762,
                  0.763,
                  0.764,
                  0.765,
                  0.766,
                  0.767,
                  0.768,
                  0.769,
                  0.77,
                  0.771,
                  0.772,
                  0.773,
                  0.774,
                  0.775,
                  0.776,
                  0.777,
                  0.778,
                  0.779,
                  0.78,
                  0.781,
                  0.782,
                  0.783,
                  0.784,
                  0.785,
                  0.786,
                  0.787,
                  0.788,
                  0.789,
                  0.79,
                  0.791,
                  0.792,
                  0.793,
                  0.794,
                  0.795,
                  0.796,
                  0.797,
                  0.798,
                  0.799,
                  0.8,
                  0.801,
                  0.802,
                  0.803,
                  0.804,
                  0.805,
                  0.806,
                  0.807,
                  0.808,
                  0.809,
                  0.81,
                  0.811,
                  0.812,
                  0.813,
                  0.814,
                  0.815,
                  0.816,
                  0.817,
                  0.818,
                  0.819,
                  0.82,
                  0.821,
                  0.822,
                  0.823,
                  0.824,
                  0.825,
                  0.826,
                  0.827,
                  0.828,
                  0.829,
                  0.83,
                  0.831,
                  0.832,
                  0.833,
                  0.834,
                  0.835,
                  0.836,
                  0.837,
                  0.838,
                  0.839,
                  0.84,
                  0.841,
                  0.842,
                  0.843,
                  0.844,
                  0.845,
                  0.846,
                  0.847,
                  0.848,
                  0.849,
                  0.85,
                  0.851,
                  0.852,
                  0.853,
                  0.854,
                  0.855,
                  0.856,
                  0.857,
                  0.858,
                  0.859,
                  0.86,
                  0.861,
                  0.862,
                  0.863,
                  0.864,
                  0.865,
                  0.866,
                  0.867,
                  0.868,
                  0.869,
                  0.87,
                  0.871,
                  0.872,
                  0.873,
                  0.874,
                  0.875,
                  0.876,
                  0.877,
                  0.878,
                  0.879,
                  0.88,
                  0.881,
                  0.882,
                  0.883,
                  0.884,
                  0.885,
                  0.886,
                  0.887,
                  0.888,
                  0.889,
                  0.89,
                  0.891,
                  0.892,
                  0.893,
                  0.894,
                  0.895,
                  0.896,
                  0.897,
                  0.898,
                  0.899,
                  0.9,
                  0.901,
                  0.902,
                  0.903,
                  0.904,
                  0.905,
                  0.906,
                  0.907,
                  0.908,
                  0.909,
                  0.91,
                  0.911,
                  0.912,
                  0.913,
                  0.914,
                  0.915,
                  0.916,
                  0.917,
                  0.918,
                  0.919,
                  0.92,
                  0.921,
                  0.922,
                  0.923,
                  0.924,
                  0.925,
                  0.926,
                  0.927,
                  0.928,
                  0.929,
                  0.93,
                  0.931,
                  0.932,
                  0.933,
                  0.934,
                  0.935,
                  0.936,
                  0.937,
                  0.938,
                  0.939,
                  0.94,
                  0.941,
                  0.942,
                  0.943,
                  0.944,
                  0.945,
                  0.946,
                  0.947,
                  0.948,
                  0.949,
                  0.95,
                  0.951,
                  0.952,
                  0.953,
                  0.954,
                  0.955,
                  0.956,
                  0.957,
                  0.958,
                  0.959,
                  0.96,
                  0.961,
                  0.962,
                  0.963,
                  0.964,
                  0.965,
                  0.966,
                  0.967,
                  0.968,
                  0.969,
                  0.97,
                  0.971,
                  0.972,
                  0.973,
                  0.974,
                  0.975,
                  0.976,
                  0.977,
                  0.978,
                  0.979,
                  0.98,
                  0.981,
                  0.982,
                  0.983,
                  0.984,
                  0.985,
                  0.986,
                  0.987,
                  0.988,
                  0.989,
                  0.99,
                  0.991,
                  0.992,
                  0.993,
                  0.994,
                  0.995,
                  0.996,
                  0.997,
                  0.998,
                  0.999
                ],
                "density_map": [
                  0.5,
                  0.4933476736006886,
                  0.4567413375486747,
                  0.3942183596576802,
                  0.3216486915168152,
                  0.25386971177161305,
                  0.0038850477825144083,
                  0.003742508194591678,
                  0.0033671983590304157,
                  0.002830968519586001,
                  0.0022670349229450704,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0.0011821215475430824,
                  0.0014624711715632845,
                  0.0017140727400161864,
                  0.0018729402503653845,
                  0.0019191359916943041,
                  0.0029342406381951255,
                  0.003078929394702555,
                  0.003121583775363517,
                  0.007453581219555391,
                  0.008393880381643869,
                  0.008470869569816812,
                  0.00916177691215584,
                  0.0092822659953349,
                  0.010942232759534643,
                  0.010817840641006837,
                  0.009427689579732928,
                  0.00881174772256039,
                  0.007984815405870609,
                  0.003802154322880201,
                  0.0037213985710763324,
                  0.0034200761979424083,
                  0.002929196417612764,
                  0.0023736688420688532,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0.009300000406114898,
                  0.011480656977717026,
                  0.013411788315280032,
                  0.014601968698773357,
                  0.014924738859155273,
                  0.016838222609716205,
                  0.016346592868180465,
                  0.015035605911637117,
                  0.013238266817162146,
                  0.011338390835019658,
                  0.0037034309582573838,
                  0.0035322222634712967,
                  0.003141068912348472,
                  0.0036650387156374918,
                  0.00339820072158475,
                  0.0015743380098329036,
                  0.004031321051130039,
                  0.004649593946058082,
                  0.0051335581928198286,
                  0.005358401497688046,
                  0.0052566281658642505,
                  0.03851556982320608,
                  0.04648920984568961,
                  0.053227145584218774,
                  0.05864730527790425,
                  0.06058534688863152,
                  0.0586018410546362,
                  0.05589439018355271,
                  0.049706430428010914,
                  0.04139786595507199,
                  0.032965527737689876,
                  0,
                  0.004608180635179286,
                  0.005674315663458574,
                  0.006603881070455419,
                  0.007160653809822722,
                  0.007299245999501241,
                  0.007180871227852606,
                  0.0066527348783720405,
                  0.005740861152901491,
                  0.004675949907370306,
                  0.003679001496315823,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0.0019243383341630556,
                  0.002431705801464039,
                  0.002952460394425129,
                  0.0033686953382975164,
                  0.0035797220603035547,
                  0.00725835497314597,
                  0.008135753768824378,
                  0.008860563921983559,
                  0.009265394663002642,
                  0.009248148799350063,
                  0.007194136125593681,
                  0.007048748179194045,
                  0.006488244574678364,
                  0.005565067477635061,
                  0.004514037603895834,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0.002048343582109583,
                  0.002562576016697192,
                  0.0030572179920493633,
                  0.00341048947808024,
                  0.0035511803159839557,
                  0.003542920564723507,
                  0.003371361311137437,
                  0.002990291701284893,
                  0.002485345441384244,
                  0.001976763773731445,
                  0.0019227370788580831,
                  0.0024237639898976827,
                  0.0029297667439583024,
                  0.0033230768552521164,
                  0.003511487259153485,
                  0.011027737115296619,
                  0.01288332250255701,
                  0.014581628980052035,
                  0.01572474447476769,
                  0.016039322237071604,
                  0.01407640946287026,
                  0.013655315793683502,
                  0.01239531870404901,
                  0.010499968488018999,
                  0.008447791458182176,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0.007154922002951435,
                  0.009061647062567553,
                  0.01104856058872992,
                  0.012678756517393783,
                  0.01354899409045495,
                  0.015508156950073678,
                  0.015632689951657182,
                  0.01496242750645236,
                  0.013546755381987657,
                  0.011749507743486832,
                  0.0034111904023104776,
                  0.0033109157392743277,
                  0.003007527712053966,
                  0.002549204082034914,
                  0.0020517666396954034,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0.015455678926353687,
                  0.019354184672609354,
                  0.023126751295448698,
                  0.02584951694584969,
                  0.026960281695529952,
                  0.026920636575190015,
                  0.025661422763317177,
                  0.022804995509628223,
                  0.018982904221798453,
                  0.015111586130319552,
                  0.004105732787707358,
                  0.005085631632515325,
                  0.005971668708302011,
                  0.006538761499824257,
                  0.006710010034984284,
                  0.006636567050277145,
                  0.006207344970372332,
                  0.005406634555805857,
                  0.004432801667679778,
                  0.0034994303452182685,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0.0038315671653723574,
                  0.004789779450121053,
                  0.005707024209985212,
                  0.0063565742300565565,
                  0.006610193238373379,
                  0.006590287519033538,
                  0.006262437750385111,
                  0.005546027803173151,
                  0.004603987239094569,
                  0.030455468488487205,
                  0.034024978016097815,
                  0.04169450683211657,
                  0.04818542756443097,
                  0.05186292209296099,
                  0.05263024710118889,
                  0.05153347349536338,
                  0.0473896862369698,
                  0.04061060989060068,
                  0.03292106314908909,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0.002026997801968945,
                  0.002502903328600359,
                  0.0029249913694859415,
                  0.00318584937703481,
                  0.0032571675709386016,
                  0.003212533977763555,
                  0.00298941987905486,
                  0.002590662091441473,
                  0.0021163834187149727,
                  0.0016676458416065854,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0.001701922041406249,
                  0.0021523575152366885,
                  0.0026171529180656953,
                  0.0029920992556283824,
                  0.003185711020894571,
                  0.0032139876543007934,
                  0.0031218776559434748,
                  0.002838664228607196,
                  0.0024081784880493084,
                  0.0019393409283885365,
                  0.0020231053133021436,
                  0.0024896750497658197,
                  0.0028949858018192222,
                  0.003136107010004632,
                  0.006692602268170207,
                  0.007545425794757989,
                  0.00822026568596236,
                  0.0085166857142981,
                  0.008375553143881708,
                  0.007964335348485662,
                  0.0061246530069200495,
                  0.005508940781263593,
                  0.004630579316680752,
                  0.010391140371229443,
                  0.008454676462621833,
                  0.010285692557443946,
                  0.01176746103339487,
                  0.012537429515167557,
                  0.014507077958182749,
                  0.014609132303435416,
                  0.013933488001473423,
                  0.012540358008423076,
                  0.010803303977776398,
                  0.0031346573488521077,
                  0.0029659312397592877,
                  0.0026143864655111667,
                  0.0021625354475961487,
                  0.0017153679477460962,
                  0,
                  0,
                  0,
                  0.10181048110133709,
                  0.1292779994536873,
                  0.15842277716411246,
                  0.18309295777552154,
                  0.1970745911289608,
                  0.1999950398633511,
                  0.1958327348506088,
                  0.18009338548403084,
                  0.1543369923297864,
                  0.12511676275359288,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0.003281488486214009,
                  0.004145037711775666,
                  0.0050290295590755775,
                  0.005732376575590579,
                  0.006085714924660379,
                  0.006130743664749135,
                  0.005941091839458617,
                  0.005385508682431323,
                  0.004556628824958896,
                  0.017282852466623148,
                  0.01711161245756978,
                  0.020563156283440454,
                  0.02314769018458414,
                  0.02429186710885055,
                  0.02433177396818675,
                  0.023336979106973535,
                  0.02088695049356051,
                  0.01748524744015399,
                  0.013965817453709777,
                  0,
                  0,
                  0,
                  0.0016322104006102184,
                  0.002059313920635553,
                  0.00249312529598663,
                  0.002833660542384466,
                  0.0030001224294577632,
                  0.010611699622267096,
                  0.012271509133495293,
                  0.013528412794712457,
                  0.014041279455960017,
                  0.013834826151277343,
                  0.01185639277588225,
                  0.010990082171015407,
                  0.00948839532625382,
                  0.01095270486792018,
                  0.01015047538508011,
                  0.004927871117571012,
                  0.005607645541985816,
                  0.005943763167868281,
                  0.0059829348026568755,
                  0.005790086712115553,
                  0.00523957460689999,
                  0.004426610389174422,
                  0.0035554823450816408,
                  0,
                  0,
                  0,
                  0.0016358553437173175,
                  0.00205875172587628,
                  0.002481306228375666,
                  0.0028037334441173394,
                  0.002952336746161855,
                  0.0029621557737574593,
                  0.002850127349116709,
                  0.0025606464754129314,
                  0.002150313602582188,
                  0.0017207271198690036,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0.013909740901067896,
                  0.01729687408290226,
                  0.02043426873474404,
                  0.02253076604534723,
                  0.023240819327807118,
                  0.023064564201037595,
                  0.021715043692735907,
                  0.019041182491534473,
                  0.018856794724228694,
                  0.0164078868201797,
                  0.004815656474744258,
                  0.005450509427756418,
                  0.007265617387476515,
                  0.0076917933798666075,
                  0.00789840919280671,
                  0.007680841804517996,
                  0.007062028299937705,
                  0.006251572502576084,
                  0.002801444241216976,
                  0.002551180783375906,
                  0.0021671755096714534,
                  0.0035345894637894663,
                  0.0022064773970720845,
                  0.0025766168042093674,
                  0.0028040716288367513,
                  0.002865227092998433,
                  0.002824666676649579,
                  0.002626352988386056,
                  0.0022742239029817203,
                  0.0018568410370701717,
                  0.0014627200357871985,
                  0,
                  0,
                  0.05225943409193625,
                  0.06539132406610251,
                  0.0780378875403259,
                  0.08708872230795368,
                  0.0923029854617042,
                  0.09251373170097206,
                  0.08855950239070605,
                  0.07914568298749484,
                  0.06638306481352386,
                  0.05338734469687315,
                  0.0027048748981324745,
                  0.002416087286954145,
                  0.002019342151333304,
                  0.0016113466884748677,
                  0,
                  0,
                  0.006002121606371323,
                  0.007582761409350084,
                  0.009202436676137545,
                  0.010493353796438917,
                  0.011144117823129273,
                  0.011228585789137942,
                  0.010884432698950614,
                  0.009870336731260039,
                  0.011278218462511464,
                  0.010420278782187447,
                  0.004512607082493473,
                  0.005175285521587032,
                  0.00697649761322138,
                  0.007421449065775958,
                  0.007678814246588905,
                  0.007534920396995043,
                  0.006974233980993687,
                  0.006190141603224164,
                  0.0027151304990402645,
                  0.0024811810742217627,
                  0.002114199314285436,
                  0.0017074463370582384,
                  0,
                  0,
                  0.002870482108133419,
                  0.0036374595564928206,
                  0.0044397436779018236,
                  0.005102332803799573,
                  0.005460579094856124,
                  0.005523940534936131,
                  0.005386969500824638,
                  0.004924875479243524,
                  0.004198035288147317,
                  0.0033912044083267323,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0.0014906468256706325,
                  0.0018778291203191927,
                  0.0022671556398400792,
                  0.0025675017776269214,
                  0.026928904562838703,
                  0.0331604624966375,
                  0.03922280363017666,
                  0.04359130050748047,
                  0.045282046320960195,
                  0.044971687531754095,
                  0.04163143168672088,
                  0.03728752384822393,
                  0.031233016064029086,
                  0.024955144057061913,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0.00169265056184588,
                  0.0020842325222158115,
                  0.002425628852248647,
                  0.002630084248910994,
                  0.002680956485338957,
                  0.0026374491378699434,
                  0.002443425560537778,
                  0.0021084740452144875,
                  0.0017173378829870892,
                  0.0013511800476149025,
                  0,
                  0.011775007176621161,
                  0.014811625952983092,
                  0.017835955317617596,
                  0.020130707111154434,
                  0.021175802908222657,
                  0.021235420881145006,
                  0.020412803494218423,
                  0.018318426762358488,
                  0.015368397264584062,
                  0.0122910659276548,
                  0,
                  0,
                  0.001657401838994899,
                  0.002042860489498348,
                  0.002380978273223985,
                  0.0025857624667499066,
                  0.0026384903882076464,
                  0.00259807318425849,
                  0.0024107203808786705,
                  0.002083373088001061,
                  0.00169866089094211,
                  0.00133717973729363,
                  0,
                  0.003011720388245123,
                  0.0037681414856586266,
                  0.004496153427712656,
                  0.005016606714643822,
                  0.006809713682516232,
                  0.0071789537444136315,
                  0.007274651324571593,
                  0.1751752467538875,
                  0.22006550105074046,
                  0.26791580608721943,
                  0.3064158446196641,
                  0.33011547565459565,
                  0.3350684780610361,
                  0.32829365478547845,
                  0.3013855271130692,
                  0.26182976615109416,
                  0.21388734636463874,
                  0.00443123067040312,
                  0.004954241063258527,
                  0.005168291424435637,
                  0.005161290502540415,
                  0.004921020429240131,
                  0.009642330697279383,
                  0.010328713604252776,
                  0.011087822568804664,
                  0.009453492454599222,
                  0.011574266326261285,
                  0.012084244232771336,
                  0.012229221389361843,
                  0.011690501515036963,
                  0.010489443805054916,
                  0.008993495996769104,
                  0.002472864656804275,
                  0.0022251673457726936,
                  0.0018710090901718631,
                  0.001498399782121939,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0.003190227971173354,
                  0.003931784461802426,
                  0.004581870527471627,
                  0.004975162163618727,
                  0.005076086626463529,
                  0.004997873481472535,
                  0.004636741314401794,
                  0.004006525611957252,
                  0.0032663459179133815,
                  0.002571121134195797,
                  0.0012609588044560996,
                  0.0016036576199745614,
                  0.0019713647332113616,
                  0.0022886813338288425,
                  0.005232044649548849,
                  0.005990633422821037,
                  0.006662971707801042,
                  0.00702603545835785,
                  0.006965486469818833,
                  0.006617533505342603,
                  0.00483331340503622,
                  0.004348636817063228,
                  0.0036561275588846615,
                  0.0029278285863617156,
                  0,
                  0.0014243511008749997,
                  0.001783940064822472,
                  0.002132300432734597,
                  0.002384210891905388,
                  0.0024874341712605354,
                  0.0024841737760615923,
                  0.002368738877183716,
                  0.002105833484201892,
                  0.0017533994844931655,
                  0.0013960471557607484,
                  0,
                  0.0059965214140442,
                  0.007440842832425693,
                  0.008761147526189405,
                  0.009622907142211765,
                  0.009897348591266683,
                  0.009804159338223862,
                  0.0091971694425377,
                  0.008034704043005549,
                  0.006601783870480708,
                  0.005217667754871245,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0.0012356818659999315,
                  0.0015701334808781002,
                  0.001926739000234981,
                  0.002231143408022157,
                  0.0024064165867925223,
                  0.0024449710376702022,
                  0.0023973466182009235,
                  0.0022092283780027143,
                  0.0018968878220596164,
                  0.001539732882490508,
                  0,
                  0.005489322891611404,
                  0.006885054441921638,
                  0.008249627111031003,
                  0.009252247214650547,
                  0.009678052439856774,
                  0.009678213275396712,
                  0.009253011069782324,
                  0.00825093385719822,
                  0.00688656228352338,
                  0.005490720259188219,
                  0,
                  0,
                  0,
                  0,
                  0.04413367131147935,
                  0.0552394661081511,
                  0.06595410425497165,
                  0.0736464969260725,
                  0.07674705261197245,
                  0.07660109878053364,
                  0.07295450069776574,
                  0.06477042206893437,
                  0.05387356781387518,
                  0.04286775699656782,
                  0.0012521636527764149,
                  0.0015850939665460037,
                  0.0019308919320247847,
                  0.0022130094212994738,
                  0.002361959169697026,
                  0.002385931274898922,
                  0.0023219874210932663,
                  0.003403522602114844,
                  0.0034227469125470028,
                  0.0034151798007402137,
                  0.0022301310671377656,
                  0.005305694660332506,
                  0.006011474018344476,
                  0.006546179307328828,
                  0.006704803987590918,
                  0.006485310276155213,
                  0.006076022186789797,
                  0.013974623928018988,
                  0.015989248172467056,
                  0.018048087613967107,
                  0.01971636250326601,
                  0.018597506528117504,
                  0.018867322213643036,
                  0.01846789261014279,
                  0.016974323429884614,
                  0.014539414349556969,
                  0.01178274453903008,
                  0,
                  0,
                  0,
                  0,
                  0.005327008047715246,
                  0.006673830842746722,
                  0.007981048413977423,
                  0.008929438825933871,
                  0.009320946155955055,
                  0.009311245947046598,
                  0.008883393253103835,
                  0.007902279752351719,
                  0.006582939277743584,
                  0.0052427739707893925,
                  0.0012980923782948141,
                  0.0016305033369541008,
                  0.001958510323744454,
                  0.002203415634705336,
                  0.0023111591019320857,
                  0.0023143742254133964,
                  0.0022186712908751367,
                  0.0033794948051774016,
                  0.0033923001203263106,
                  0.003366465958188198,
                  0.002243067892383514,
                  0.002308496721234805,
                  0.0022877053822158515,
                  0.0021477896422434175,
                  0.001877857066118707,
                  0.0015438815539218953,
                  0.0012205839791383036,
                  0.0055917877365997395,
                  0.006930903950213077,
                  0.008146656701303552,
                  0.008930460182889186,
                  0.009171918641294376,
                  0.00907674596129615,
                  0.008498951285528411,
                  0.0074107406987986065,
                  0.006080741367265403,
                  0.004802374235076821,
                  0.0014233090678875391,
                  0.0017561175970413092,
                  0.0020498888846447474,
                  0.0022298729610228493,
                  0.0022778370071944772,
                  0.002245045504854621,
                  0.002086533626412668,
                  0.0018060321357791316,
                  0.0014741460946386604,
                  0.0011610822433030926,
                  0,
                  0,
                  0,
                  0.0013827463903794215,
                  0.0017123579653489016,
                  0.0020099652771815306,
                  0.002199946846204788,
                  0.002256904013979241,
                  0.002231740066279509,
                  0.002086590197460617,
                  0.0018167254102469952,
                  0.0014890824533179306,
                  0.0034741881857478524,
                  0.0029170197814308986,
                  0.003569816181006497,
                  0.004117809899187263,
                  0.00442351550204387,
                  0.004484050641403822,
                  0.004384741586832451,
                  0.08766479856113372,
                  0.10780965218616599,
                  0.12676972624150495,
                  0.13883506749958976,
                  0.1442217050792369,
                  0.14388014483792944,
                  0.13661560845396484,
                  0.1209138440562995,
                  0.10048862916207885,
                  0.08011824253849235,
                  0.0019127462674948643,
                  0.0016030803757262873,
                  0.0012812971601870332,
                  0.005400598455565182,
                  0.006692443184993616,
                  0.00786367555310426,
                  0.008616921467131309,
                  0.00884741317110432,
                  0.008753907616883844,
                  0.01065565587499951,
                  0.010234794704616869,
                  0.009574603201085672,
                  0.008808301812318908,
                  0.0043877984267666915,
                  0.004394517696263,
                  0.004213941990992432,
                  0.003770585400783453,
                  0.0031558481462126754,
                  0.002520329637546562,
                  0.0013756802979105658,
                  0.0016953413379064905,
                  0.001975460081053357,
                  0.004794322435288835,
                  0.005474813557399351,
                  0.006022266165959238,
                  0.006244493957117974,
                  0.006091998112082986,
                  0.005730631695874504,
                  0.005161218722712215,
                  0.0035390789112271473,
                  0.0029067781493571513,
                  0.00348743202781065,
                  0.0014991846140754472,
                  0.0018086927584041765,
                  0.002046364570549017,
                  0.0021573773988166687,
                  0.0021658150257202083,
                  0.0032020643544162855,
                  0.0032916183486372307,
                  0.0033065796379749234,
                  0.020576771714793014,
                  0.024157462427609806,
                  0.029216356774828416,
                  0.033490473047676196,
                  0.035835367197465995,
                  0.036130880458583196,
                  0.03518074470520655,
                  0.033860097687732876,
                  0.030111765867769497,
                  0.025645005483794538,
                  0.005453894211962317,
                  0.0058789715589818055,
                  0.006124448690128843,
                  0.006049403303462457,
                  0.005607661335753866,
                  0.004970319351166769,
                  0.004249730362908269,
                  0.001757311868472835,
                  0.001448938687579426,
                  0.0011473019737021578,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0.009256945665169677,
                  0.011663768744765874,
                  0.01408719766104635,
                  0.015961133645793116,
                  0.016849206587101546,
                  0.01692610352640172,
                  0.016322854266217185,
                  0.014705610259888176,
                  0.0123775223171112,
                  0.009918670991100529,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0.0021626291558322773,
                  0.0027419380843726293,
                  0.0033501568835823075,
                  0.004930719299214524,
                  0.005495913657669573,
                  0.005850822527472292,
                  0.006004990952831851,
                  0.005800268008262476,
                  0.005279416741803904,
                  0.004620185242937348,
                  0.001869331611896318,
                  0.0015971528094384257,
                  0.0034248819875564067,
                  0.002705541461406362,
                  0.0033093201548148243,
                  0.0038145711263872914,
                  0.004094743138305857,
                  0.004149075222489646,
                  0.0040550735660261385,
                  0.003718823080637759,
                  0.0031789016773076614,
                  0.002572697460581803,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0.0010849269093701403,
                  0.001372336941070821,
                  0.0016693040797700653,
                  0.010658195015974883,
                  0.013087929188189395,
                  0.01547035516945971,
                  0.01729875440111478,
                  0.01807216619683319,
                  0.017923100901379496,
                  0.01712494955879274,
                  0.014408519200525174,
                  0.012197883627417078,
                  0.010939844828081219,
                  0.001420705733640925,
                  0.0017098775414812533,
                  0.0019285398175465712,
                  0.002027399843105309,
                  0.0020324839353620607,
                  0.0019526146674341206,
                  0.0017510549928926446,
                  0.0014682235356433594,
                  0.0011738257954869277,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0.019606502861715395,
                  0.024313848281301672,
                  0.0286005678888702,
                  0.031379387758671426,
                  0.032248214456495346,
                  0.03192734585972676,
                  0.029919577532411843,
                  0.026110363491072756,
                  0.022465626671723436,
                  0.018240626493399387,
                  0.0015964206447289424,
                  0.0018409935502727865,
                  0.0019771306412294937,
                  0.0020038829973326525,
                  0.0019591277745188117,
                  0.0017975347325166844,
                  0.0015372251675769527,
                  0.0034737089910518203,
                  0.0028000851502869776,
                  0.00336327992542448,
                  0.004931233641647252,
                  0.005403607290541217,
                  0.005684869706487335,
                  0.005716492197568957,
                  0.005391721023793164,
                  0.004829990944300036,
                  0.004158189050790314,
                  0.0016674755631389566,
                  0.0013849970696023675,
                  0.0011011706597719004,
                  0,
                  0,
                  0,
                  0,
                  0.004256866559146852,
                  0.005370339501322327,
                  0.006500703209307197,
                  0.008492310621645249,
                  0.009206826050811998,
                  0.009530169875037301,
                  0.009473226833567619,
                  0.008829126734912218,
                  0.0077573284288701225,
                  0.0065291875493307325,
                  0.0016749675082884143,
                  0.0013997164236034109,
                  0.319095306469877,
                  0.39097479998322865,
                  0.4540530607796899,
                  0.4912129162231923
                ],
                "algorithm_manifest": {
                  "name": "core_terrain_scale",
                  "mode": "valley",
                  "window_size": 0.01,
                  "lens_profile": "gravitational"
                }
              },
              "name": "terrain_scale_5_valley",
              "base_frequency": 220.0,
              "notes": [
                {
                  "log_position": 0.011,
                  "frequency": 221.6838272903109,
                  "midi": 57,
                  "cents_from_base": 13.2,
                  "prime_sources": []
                },
                {
                  "log_position": 0.2,
                  "frequency": 252.71363809934772,
                  "midi": 59,
                  "cents_from_base": 240.0,
                  "prime_sources": []
                },
                {
                  "log_position": 0.402,
                  "frequency": 290.6944492448183,
                  "midi": 62,
                  "cents_from_base": 482.40000000000003,
                  "prime_sources": []
                },
                {
                  "log_position": 0.609,
                  "frequency": 335.54436371638246,
                  "midi": 64,
                  "cents_from_base": 730.8,
                  "prime_sources": []
                },
                {
                  "log_position": 0.873,
                  "frequency": 402.9228220239755,
                  "midi": 67,
                  "cents_from_base": 1047.6,
                  "prime_sources": []
                }
              ]
            }
            ```

        **readmes/**

            `readmes/code_paste_template.md`
            ```md
            # Prime Scale App – Code Template (Clean Paste Structure)
            
            This markdown provides clean headings and fenced code blocks for you to manually paste in each script's full content.
            
            ---
            
            ## scale_utils.py
            
            ```python
            # Paste full contents of scale_utils.py here
            import math
            import json
            import os
            
            def generate_primes(n):
                primes = [2]
                candidate = 3
                while len(primes) < n:
                    is_prime = True
                    for p in primes:
                        if candidate % p == 0:
                            is_prime = False
                            break
                        if p * p > candidate:
                            break
                    if is_prime:
                        primes.append(candidate)
                    candidate += 2
                return primes
            
            def reduce_value(val):
                while val >= 2:
                    val /= 2
                while val < 1:
                    val *= 2
                return val
            
            def get_log_positions(primes):
                """Return log2 positions of primes reduced to the 1–2 octave range."""
                return [math.log2(reduce_value(p)) for p in primes]
            
            def generate_density_axis(resolution):
                """Returns evenly spaced samples from 0 to 1 (not inclusive) for log-space rendering."""
                return [i / resolution for i in range(resolution)]
            
            def circular_distance(a, b):
                return min(abs(a - b), 1 - abs(a - b))
            
            def prime_weight(p, curve=1.0):
                if curve == 0.0:
                    return 1.0
                return 1 / (p ** curve)
            
            def add_bounds(notes, base_freq):
                bounds = [
                    {
                        "log_position": 0.0,
                        "frequency": base_freq,
                        "midi": round(69 + 12 * math.log2(base_freq / 440.0)),
                        "cents_from_base": 0.0,
                        "prime_sources": []
                    },
                    {
                        "log_position": 1.0,
                        "frequency": base_freq * 2,
                        "midi": round(69 + 12 * math.log2((base_freq * 2) / 440.0)),
                        "cents_from_base": 1200.0,
                        "prime_sources": []
                    }
                ]
                return [bounds[0]] + notes + [bounds[1]]
            
            def export_json(scale_data, filename):
                # Always write to top-level /output/ folder
                script_dir = os.path.dirname(os.path.abspath(__file__))
                project_root = os.path.dirname(script_dir)
                output_dir = os.path.join(project_root, "output")
            
                os.makedirs(output_dir, exist_ok=True)
                full_path = os.path.join(output_dir, os.path.basename(filename))
            
                with open(full_path, "w", encoding="utf-8") as f:
                    json.dump(scale_data, f, indent=2)
            
                print(f"✔ Saved scale to {full_path}")
            ```
            
            ---
            
            ## core_terrain_scale.py
            
            ```python
            # Paste full contents of core_terrain_scale.py here
            import argparse
            import math
            from scripts.scale_utils import (
                generate_primes,
                get_log_positions,
                prime_weight,
                circular_distance,
                generate_density_axis,
                add_bounds,
                export_json
            )
            
            # Terrain-specific smoothing function
            def gravitational_fade(d, w, n=2.5):
                relative = d / (w / 2)
                return 1 / (1 + (relative ** n))
            
            # Generate density map across log2-reduced space
            def generate_density_map(log_positions, weights, resolution, window_size):
                x_axis = generate_density_axis(resolution)
                density_map = []
            
                for x in x_axis:
                    total_weight = 0
                    for log_pos, weight in zip(log_positions, weights):
                        distance = circular_distance(log_pos, x)
                        if distance <= window_size / 2:
                            focus = gravitational_fade(distance, window_size)
                            total_weight += weight * focus
                    density_map.append(total_weight)
            
                return x_axis, density_map
            
            # Segment and select notes from density map
            def select_notes_from_density(x_axis, density_map, num_notes, base_frequency, mode):
                segment_width = 1.0 / num_notes
                selected_notes = []
            
                for i in range(num_notes):
                    segment_start = i * segment_width
                    segment_end = segment_start + segment_width
                    segment_range = [(x, d) for x, d in zip(x_axis, density_map) if segment_start <= x < segment_end]
            
                    if segment_range:
                        best_x, _ = min(segment_range, key=lambda t: t[1]) if mode == "valley" else max(segment_range, key=lambda t: t[1])
                        freq = base_frequency * (2 ** best_x)
                        selected_notes.append({
                            "log_position": best_x,
                            "frequency": freq,
                            "midi": round(69 + 12 * math.log2(freq / 440.0)),
                            "cents_from_base": 1200 * best_x,
                            "prime_sources": []
                        })
            
                return selected_notes
            
            # Full generator function
            def generate_terrain_scale(prime_count, base_frequency, num_notes, window_size, density_resolution, mode, include_bounds=True, weight_curve=1.0):
                primes = generate_primes(prime_count)
                log_positions = get_log_positions(primes)
                weights = [prime_weight(p, weight_curve) for p in primes]
            
                x_axis, density_map = generate_density_map(log_positions, weights, density_resolution, window_size)
                selected_notes = select_notes_from_density(x_axis, density_map, num_notes, base_frequency, mode)
            
                if include_bounds:
                    selected_notes = add_bounds(selected_notes, base_frequency)
            
                scale_data = {
                    "name": f"terrain_scale_{num_notes}_{mode}",
                    "base_frequency": base_frequency,
                    "notes": selected_notes
                }
            
                filename = f"output/terrain_scale_{num_notes}_{mode}.json"
                export_json(scale_data, filename)
            
            # CLI runner
            if __name__ == "__main__":
                parser = argparse.ArgumentParser()
                parser.add_argument("--prime-count", type=int, default=1000)
                parser.add_argument("--base-frequency", type=float, default=220.0)
                parser.add_argument("--num-notes", type=int, default=8)
                parser.add_argument("--window-size", type=float, default=0.007)
                parser.add_argument("--density-resolution", type=int, default=4000)
                parser.add_argument("--mode", choices=["valley", "peak"], default="valley")
                parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
                parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
                parser.add_argument("--weight-curve", type=float, default=1.0)
                parser.set_defaults(include_bounds=True)
            
                args = parser.parse_args()
            
                generate_terrain_scale(
                    prime_count=args.prime_count,
                    base_frequency=args.base_frequency,
                    num_notes=args.num_notes,
                    window_size=args.window_size,
                    density_resolution=args.density_resolution,
                    mode=args.mode,
                    include_bounds=args.include_bounds,
                    weight_curve=args.weight_curve
                )
            ```
            
            ---
            
            ## gap_threshold_scout.py
            
            ```python
            # Paste full contents of gap_threshold_scout.py here
            import argparse
            import math
            from scripts.scale_utils import (
                generate_primes,
                get_log_positions,
                add_bounds,
                export_json,
                generate_density_axis  # included for compatibility or plotting if needed
            )
            
            # Count qualifying gaps for a given threshold
            def detect_gap_count(log_positions, threshold):
                log_positions.sort()
                gap_centers = []
            
                for i in range(len(log_positions) - 1):
                    gap = log_positions[i + 1] - log_positions[i]
                    if gap >= threshold:
                        center_log = (log_positions[i] + log_positions[i + 1]) / 2
                        gap_centers.append(center_log)
            
                return gap_centers
            
            # Scan thresholds to find ones that match note goal
            def scan_thresholds(prime_count, threshold_min, threshold_max, step_size, note_goal, tolerance, base_frequency, include_bounds, density_resolution):
                primes = generate_primes(prime_count)
                log_positions = get_log_positions(primes)
                matches = []
            
                # Optional: could use this for visual overlays or precision matching later
                _ = generate_density_axis(density_resolution)
            
                current = threshold_min
                while current <= threshold_max:
                    gap_centers = detect_gap_count(log_positions, current)
                    count = len(gap_centers)
            
                    if abs(count - note_goal) <= tolerance:
                        print(f"✔ Match: {count} notes at threshold {current:.6f}")
                        matches.append((current, count, gap_centers))
                    else:
                        print(f"... Skipped: {count} notes at threshold {current:.6f}")
            
                    current = round(current + step_size, 10)  # Avoid float rounding errors
            
                if matches:
                    best_thresh, best_count, best_centers = matches[0]
                    notes = []
                    for log_pos in best_centers:
                        freq = base_frequency * (2 ** log_pos)
                        notes.append({
                            "log_position": log_pos,
                            "frequency": freq,
                            "midi": round(69 + 12 * math.log2(freq / 440.0)),
                            "cents_from_base": 1200 * log_pos,
                            "prime_sources": []
                        })
            
                    if include_bounds:
                        notes = add_bounds(notes, base_frequency)
            
                    scale_data = {
                        "name": f"gap_scout_match_{best_count}_notes",
                        "base_frequency": base_frequency,
                        "notes": notes
                    }
            
                    export_json(scale_data, f"gap_scout_match_{best_count}_notes.json")
                else:
                    print("No matching thresholds found within specified range.")
            
            if __name__ == "__main__":
                parser = argparse.ArgumentParser()
                parser.add_argument("--prime-count", type=int, required=True)
                parser.add_argument("--base-frequency", type=float, default=220.0)
                parser.add_argument("--threshold-range", nargs=2, type=float, required=True, metavar=("MIN", "MAX"))
                parser.add_argument("--step-size", type=float, default=0.001)
                parser.add_argument("--note-goal", type=int, required=True)
                parser.add_argument("--tolerance", type=int, default=1)
                parser.add_argument("--density-resolution", type=int, default=4000)
                parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
                parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
                parser.set_defaults(include_bounds=True)
            
                args = parser.parse_args()
            
                scan_thresholds(
                    prime_count=args.prime_count,
                    threshold_min=args.threshold_range[0],
                    threshold_max=args.threshold_range[1],
                    step_size=args.step_size,
                    note_goal=args.note_goal,
                    tolerance=args.tolerance,
                    base_frequency=args.base_frequency,
                    include_bounds=args.include_bounds,
                    density_resolution=args.density_resolution
                )
            
            ```
            
            ---
            
            ## core_pure_prime_scale.py
            
            ```python
            # Paste full contents of core_pure_prime_scale.py here
            import argparse
            import math
            from scripts.scale_utils import (
                generate_primes,
                get_log_positions,
                add_bounds,
                export_json,
                generate_density_axis  # included for compatibility and visualization
            )
            
            def generate_pure_prime_scale(prime_count, base_frequency, include_bounds=True, density_resolution=4000):
                primes = generate_primes(prime_count)
                log_positions = get_log_positions(primes)
            
                # Optional: generate axis for any future visualization
                _ = generate_density_axis(density_resolution)
            
                notes = []
                for log_pos in log_positions:
                    freq = base_frequency * (2 ** log_pos)
                    notes.append({
                        "log_position": log_pos,
                        "frequency": freq,
                        "midi": round(69 + 12 * math.log2(freq / 440.0)),
                        "cents_from_base": 1200 * log_pos,
                        "prime_sources": []
                    })
            
                if include_bounds:
                    notes = add_bounds(notes, base_frequency)
            
                scale_data = {
                    "name": f"pure_prime_scale_{prime_count}_primes",
                    "base_frequency": base_frequency,
                    "notes": notes
                }
            
                export_json(scale_data, f"pure_prime_scale_{prime_count}_primes.json")
            
            if __name__ == "__main__":
                parser = argparse.ArgumentParser()
                parser.add_argument("--prime-count", type=int, required=True)
                parser.add_argument("--base-frequency", type=float, default=220.0)
                parser.add_argument("--density-resolution", type=int, default=4000)
                parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
                parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
                parser.set_defaults(include_bounds=True)
            
                args = parser.parse_args()
            
                generate_pure_prime_scale(
                    prime_count=args.prime_count,
                    base_frequency=args.base_frequency,
                    include_bounds=args.include_bounds,
                    density_resolution=args.density_resolution
                )
            
            ```
            
            ---
            
            ## binary_gap_analyzer.py
            
            ```python
            # Paste full contents of binary_gap_analyzer.py here
            
            import math
            
            def reduce_value(x):
                while x >= 2:
                    x /= 2
                return x
            
            def generate_primes(n):
                primes = []
                candidate = 2
                while candidate <= n:
                    is_prime = True
                    for p in primes:
                        if p * p > candidate:
                            break
                        if candidate % p == 0:
                            is_prime = False
                            break
                    if is_prime:
                        primes.append(candidate)
                    candidate += 1
                return primes
            
            def compute_reduced_primes(tier):
                primes = generate_primes(tier)
                reduced = [reduce_value(p) for p in primes]
                return sorted(reduced), primes
            
            def compute_segment_gaps(reduced, tier):
                segment_width = 1 / (tier // 2)
                segments = []
                for i in range(len(reduced) - 1):
                    start = reduced[i]
                    end = reduced[i + 1]
                    gap = end - start
                    segment_count = round(gap / segment_width)
                    segments.append((start, end, segment_count))
                return segments, segment_width
            
            ```
            
            ---
            
            ## cluster_finder.py
            
            ```python
            # Paste full contents of cluster_finder.py here
            
            import argparse
            from binary_gap_analyzer import compute_reduced_primes, compute_segment_gaps
            import math
            
            def log_center(start, end):
                return math.sqrt(start * end)
            
            def find_clusters(segments, threshold=4):
                clusters = []
                current_cluster = []
                for start, end, count in segments:
                    if count >= threshold:
                        if current_cluster:
                            clusters.append(current_cluster)
                            current_cluster = []
                    else:
                        current_cluster.append((start, end))
                if current_cluster:
                    clusters.append(current_cluster)
                return clusters
            
            def main():
                parser = argparse.ArgumentParser(description="Cluster Finder based on segment gaps.")
                parser.add_argument("--tier", type=int, required=True, help="Binary segmentation tier (must be power of two)")
                args = parser.parse_args()
            
                reduced, _ = compute_reduced_primes(args.tier)
                segment_data, segment_width = compute_segment_gaps(reduced, args.tier)
            
                clusters = find_clusters(segment_data)
            
                print(f"Tier: {args.tier} | Segment Width: {segment_width:.6f}")
                print(f"Found {len(clusters)} cluster(s):\n")
            
                for idx, cluster in enumerate(clusters):
                    cluster_start = cluster[0][0]
                    cluster_end = cluster[-1][1]
                    center = log_center(cluster_start, cluster_end)
                    print(f"Cluster {idx + 1}:")
                    print(f"  Range: {cluster_start:.6f} -> {cluster_end:.6f}")
                    print(f"  Log Center: {center:.6f}")
                    print(f"  Members: {len(cluster)} segments\n")
            
            if __name__ == "__main__":
                main()
            
            ```
            
            ---
            
            ## main.py (planned CLI entry point)
            
            ```python
            # Paste full contents of main.py when implemented
            """
            Prime Scale App – CLI Entry Point
            
            Usage (run from project root):
              python -m scripts.main --scale-type terrain ...
              python -m scripts.main --scale-type gap ...
              python -m scripts.main --scale-type pure ...
            """
            
            import argparse
            from scripts.core_terrain_scale import generate_terrain_scale
            from scripts.gap_threshold_scout import scan_thresholds
            from scripts.core_pure_prime_scale import generate_pure_prime_scale
            
            def main():
                parser = argparse.ArgumentParser(description="Prime Scale Generator CLI")
                subparsers = parser.add_subparsers(dest="scale_type", required=True, help="Scale type to generate")
            
                # Terrain scale CLI
                terrain_parser = subparsers.add_parser("terrain", help="Generate terrain-based scale")
                terrain_parser.add_argument("--prime-count", type=int, default=1000)
                terrain_parser.add_argument("--base-frequency", type=float, default=220.0)
                terrain_parser.add_argument("--num-notes", type=int, default=8)
                terrain_parser.add_argument("--window-size", type=float, default=0.007)
                terrain_parser.add_argument("--density-resolution", type=int, default=4000)
                terrain_parser.add_argument("--mode", choices=["valley", "peak"], default="valley")
                terrain_parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
                terrain_parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
                terrain_parser.add_argument("--weight-curve", type=float, default=1.0)
                terrain_parser.set_defaults(include_bounds=True)
            
                # Gap scale CLI
                gap_parser = subparsers.add_parser("gap", help="Generate gap-based scale")
                gap_parser.add_argument("--prime-count", type=int, required=True)
                gap_parser.add_argument("--base-frequency", type=float, default=220.0)
                gap_parser.add_argument("--threshold-range", nargs=2, type=float, required=True, metavar=("MIN", "MAX"))
                gap_parser.add_argument("--step-size", type=float, default=0.001)
                gap_parser.add_argument("--note-goal", type=int, required=True)
                gap_parser.add_argument("--tolerance", type=int, default=1)
                gap_parser.add_argument("--density-resolution", type=int, default=4000)
                gap_parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
                gap_parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
                gap_parser.set_defaults(include_bounds=True)
            
                # Pure scale CLI
                pure_parser = subparsers.add_parser("pure", help="Generate raw prime scale")
                pure_parser.add_argument("--prime-count", type=int, required=True)
                pure_parser.add_argument("--base-frequency", type=float, default=220.0)
                pure_parser.add_argument("--density-resolution", type=int, default=4000)
                pure_parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
                pure_parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
                pure_parser.set_defaults(include_bounds=True)
            
                args = parser.parse_args()
            
                if args.scale_type == "terrain":
                    generate_terrain_scale(
                        prime_count=args.prime_count,
                        base_frequency=args.base_frequency,
                        num_notes=args.num_notes,
                        window_size=args.window_size,
                        density_resolution=args.density_resolution,
                        mode=args.mode,
                        include_bounds=args.include_bounds,
                        weight_curve=args.weight_curve
                    )
            
                elif args.scale_type == "gap":
                    scan_thresholds(
                        prime_count=args.prime_count,
                        threshold_min=args.threshold_range[0],
                        threshold_max=args.threshold_range[1],
                        step_size=args.step_size,
                        note_goal=args.note_goal,
                        tolerance=args.tolerance,
                        base_frequency=args.base_frequency,
                        include_bounds=args.include_bounds,
                        density_resolution=args.density_resolution
                    )
            
                elif args.scale_type == "pure":
                    generate_pure_prime_scale(
                        prime_count=args.prime_count,
                        base_frequency=args.base_frequency,
                        include_bounds=args.include_bounds,
                        density_resolution=args.density_resolution
                    )
            
            if __name__ == "__main__":
                main()
            ```
            ```

            `readmes/final_architecture_README.md`
            ```md
            # Prime Scale App: Final Architecture & Packaging Strategy
            
            _Last updated: 2025-05-06_
            
            This README consolidates and replaces previous frontend and architecture planning documents. It defines the final architecture and development direction for the Prime Scale App as a modular, JavaScript-based APK-ready environment.
            
            ---
            
            ## Core Principles
            
            - **Frontend-first, JavaScript-native**
            - **APK and PWA compatible** (Capacitor.js recommended)
            - **Modular algorithm support** via drop-in JavaScript packages
            - **No Python dependency required** for scale generation
            - **Developer- and user-friendly** with hot-loadable modules and clean packaging
            
            ---
            
            ## Directory Structure
            
            ```
            /prime-scale-app/
            ├── /public/               # Static assets (icon, manifest, splash)
            ├── /src/
            │   ├── /modules/          # Scale algorithm modules (JS)
            │   ├── /components/       # React components (tool popups, viewers, tray)
            │   ├── /utils/            # Shared JS utilities (e.g. note conversion)
            │   ├── /data/             # modules.json manifest + preloaded scales
            │   └── App.jsx            # Main React app shell
            ├── /output/               # User-generated JSON scales (persistent)
            ├── /android/              # APK wrapper config (via Capacitor)
            ├── /README.md             # (This file)
            └── vite.config.js         # Vite bundler setup
            ```
            
            ---
            
            ## Modular Loader System
            
            Each module is a self-contained JavaScript file exporting a single generator function.
            
            ### Example module (e.g., `/src/modules/terrain.js`):
            ```js
            export function generateTerrainScale(config) {
              // ...implementation...
              return {
                name: "terrain_scale_8_notes",
                base_frequency: config.baseFrequency,
                notes: [...]
              };
            }
            ```
            
            ### Module manifest (`/src/data/modules.json`):
            ```json
            [
              {
                "id": "terrain",
                "label": "Terrain Scale",
                "type": "generator",
                "entry": "../modules/terrain.js",
                "function": "generateTerrainScale"
              },
              {
                "id": "gap",
                "label": "Gap Scale",
                "type": "generator",
                "entry": "../modules/gap.js",
                "function": "generateGapScale"
              }
            ]
            ```
            
            Modules are auto-loaded and attached to the front-end dropdowns at runtime. **No manual editing of `main` or app code is required.**
            
            ---
            
            ## App Features
            
            - Modular **tool pop-ups** with real-time previews
            - Scrollable and zoomable **multi-scale number line**
            - Bottom **note tray** for collecting and combining notes
            - **Playback engine** using Web Audio API
            - Export any scale or tray as `.json`
            - **Plugin-ready interface** for advanced tools and effects
            
            ---
            
            ## Packaging Options
            
            - **PWA (Progressive Web App)**
              - One-click install on Android
              - Offline-capable
              - Native-like UI and splash screen
            - **APK (Android)**
              - Wrap React frontend using **Capacitor.js**
              - Add native hooks if needed later (e.g. file system)
            
            ---
            
            ## Developer Guidelines
            
            - All core scale logic should live in `/src/modules/` as ES modules.
            - Add new tools by:
              1. Writing the JS module
              2. Updating `modules.json`
            - Shared functions (prime generation, reduction, etc.) go in `/src/utils/`
            - Always export scales to `/output/` so they can be viewed, played, or edited
            
            ---
            
            ## Roadmap Highlights
            
            - [x] Migrate all core algorithms to JavaScript
            - [x] Design final plugin loading system
            - [x] Enable modular UI dropdowns
            - [ ] Add metadata overlay for long-tap previews
            - [ ] Build native APK shell via Capacitor.js
            - [ ] Optional: GitHub-hosted web version for desktop testing
            
            ---
            
            This document now serves as the **canonical reference** for the app's total architecture and frontend goals.
            ```

            `readmes/nextgen_README_consolidated.md`
            ```md
            Prime Scale App – Modular Rewrite (In Progress)
            
            ## Purpose
            This README documents the ongoing modular refactor of the Prime Scale App. Its goal is to offer a clean, scalable, and extensible architecture that supports multiple scale-generation algorithms and prepares the codebase for future CLI, GUI, and web-based interfaces.
            
            ---
            
            ## Project Goals
            - Modular core scale types
            - Reusable utilities for primes, reduction, weighting, and export
            - CLI interface to choose and configure scale types
            - Future-ready for GUI or Web front-end
            
            ---
            
            ## Directory Structure (Target)
            ```
            /prime-scale-app/
            ├── scripts/
            │   ├── core_terrain_scale.py              # Terrain-based density generator
            │   ├── core_gap_scale.py                  # Gap-based note detection (WIP)
            │   ├── core_pure_prime_scale.py           # Raw prime tone sequence
            │   ├── core_cluster_scale.py              # Density-based cluster detection (WIP)
            │   ├── scale_utils.py                     # Shared utilities and exports
            │   ├── main.py                            # CLI entry point (planned)
            │   └── __init__.py                        # Package init
            ├── output/                                # Generated scale .json files
            ├── interface/                             # Optional HTML or GUI code
            ├── README.md                              # Legacy reference
            ├── nextgen_README.md                      # This file – active documentation
            ```
            
            ---
            
            ## Shared Utilities (`scale_utils.py`)
            Implements common functionality:
            - `generate_primes(n)`
            - `reduce_value(val)`
            - `get_log_positions(primes)`
            - `generate_density_axis(resolution)`
            - `circular_distance(a, b)`
            - `prime_weight(p, curve)`
            - `add_bounds(notes, base_freq)` – Adds base and octave markers
            - `export_json(scale_data, filename)` – Saves output to `/output/`
            
            Note: `density_resolution` is included in many modules for future plotting/visualization but may currently be unused. Commented accordingly.
            
            ---
            
            ## Scale Types
            
            ### 1. Terrain-Based Scale (`core_terrain_scale.py`)
            Generates a weighted density map of reduced primes, tiles the log2 octave, and selects either valleys or peaks within segments.
            - Uses gravity-style smoothing for density fade
            - Fully implemented CLI interface
            
            **Arguments**: `--prime-count`, `--base-frequency`, `--num-notes`, `--window-size`, `--density-resolution`, `--mode` (valley/peak), `--include-bounds`, `--weight-curve`
            
            ### 2. Gap-Based Scale (`gap_threshold_scout.py`)
            Scans through gap thresholds between log-reduced primes, selecting gaps that match a target note count.
            - Outputs matching scales to JSON
            - CLI runner implemented
            
            **Arguments**: `--threshold-range`, `--note-goal`, `--tolerance`, `--step-size`, `--prime-count`, `--base-frequency`, `--include-bounds`
            
            Note: `density_resolution` is currently unused (commented).
            
            ### 3. Pure Prime Scale (`core_pure_prime.py`)
            Maps raw reduced primes into pitch space with no filtering.
            - Simplest generator, clean reference
            
            **Arguments**: `--prime-count`, `--base-frequency`, `--include-bounds`, `--density-resolution` *(commented if unused)*
            
            ### 4. Cluster Scale (WIP)
            Combines:
            - `binary_gap_analyzer.py`: Computes binary-segment gaps from reduced primes
            - `cluster_finder.py`: Identifies sparse clusters by filtering gap counts
            
            **Current output is CLI print only – no JSON export yet.**
            
            **Next Steps**:
            - Convert clusters into scale notes
            - Integrate export using `scale_utils.py`
            - Add CLI wrapper for standalone cluster scale
            
            ---
            
            ## Planned CLI Interface (`main.py`)
            Single unified entry point to route commands to different generators.
            
            **Examples:**
            ```sh
            python main.py \
              --scale-type gap \
              --prime-count 2000 \
              --base-frequency 220.0 \
              --gap-threshold 0.012 \
              --sort-by pitch \
              --include-bounds
            
            python main.py \
              --scale-type pure \
              --prime-count 128 \
              --base-frequency 220.0 \
              --order pitch
            
            python main.py \
              --scale-type cluster \
              --prime-count 3000 \
              --base-frequency 220.0 \
              --cluster-sensitivity 0.85 \
              --sort-by strength
            ```
            
            ---
            
            ## Transition Checklist
            
            ### Core Modules:
            - [x] `scale_utils.py` created and shared across all scripts
            - [x] `core_terrain_scale.py` refactored and validated
            - [x] `gap_threshold_scout.py` implemented and debugged
            - [x] `core_pure_prime.py` implemented
            - [ ] `core_cluster_scale.py` to be completed (cluster → note export + CLI)
            
            ### CLI Integration:
            - [ ] Create `main.py` driver with `argparse` routing to each core
            - [ ] Define scale types and attach to handlers in `main.py`
            - [ ] Add validation and unified `--help` messaging
            
            ### Output & Interface:
            - [x] Centralized all JSON exports to `/output/`
            - [ ] GUI or HTML playback (optional – future scope)
            
            ---
            
            ## Notes
            - All scripts use `include_bounds` to optionally add octave anchors.
            - `density_resolution` is present in several modules for consistency, even if not currently used.
            - This file replaces the legacy `README.md` as the living source of documentation.
            - Future additions (e.g. scale metadata, UI metadata flags, performance tweaks) will be tracked here.
            
            ---
            
            ## Dev Guidance
            - Comment out unused arguments (like `density_resolution`) but leave them in place for consistency.
            - Use `scale_utils.py` exclusively for shared logic.
            - Avoid duplicating export or reduction code in core modules.
            - Add CLI wrappers to all future modules.
            
            ---
            
            Let this README grow with the system – all additions should be documented here as they stabilize.
            
            **Next priority: Finish cluster → note export + `main.py` CLI router.**
            ```

            `readmes/prime_scale_cheatsheet_fullpath.txt`
            ```txt
            # PRIME SCALE APP – FULL PATH + MODULE EXECUTION CLI CHEATSHEET
            
            ## TERRAIN SCALE
            cd /storage/emulated/0/Documents/prime-scale-app 
            python -m scripts.main terrain \
              --prime-count 1000 \
              --base-frequency 220.0 \
              --num-notes 8 \
              --window-size 0.007 \
              --density-resolution 4000 \
              --mode valley \
              --weight-curve 1.0 \
              --include-bounds
            
            ## GAP SCALE
            cd /storage/emulated/0/Documents/prime-scale-app
            python -m scripts.main gap --prime-count 1000 --base-frequency 220.0 --threshold-range 0.01 0.05 --step-size 0.001 --note-goal 9 --tolerance 1
            
            ## PURE PRIME SCALE
            cd /storage/emulated/0/Documents/prime-scale-app 
            python -m scripts.main pure \
              --prime-count 128 \
              --base-frequency 220.0 \
              --density-resolution 4000 \
              --include-bounds
            
            ## CLUSTER ANALYSIS (WIP - OUTPUT TO TERMINAL ONLY)
            cd /storage/emulated/0/Documents/prime-scale-app 
            python -m scripts.main cluster \
              --tier 128
            
            ## NOTE:
            # These assume your working directory is set to: /storage/emulated/0/Documents/prime-scale-app
            # If not, cd into that directory or adjust accordingly.
            ```

            `readmes/prime_scale_drive_scripts_README.md`
            ```md
            # Prime Scale App – Mobile Backup & Restore Scripts
            
            These bash scripts let you safely **backup and restore** your Prime Scale App project directory to and from Google Drive using `rclone`. Works entirely on Android via Termux.
            
            ---
            
            ## 1. Backup Script
            
            **File:** `backup_to_drive.sh`
            
            ```bash
            #!/data/data/com.termux/files/usr/bin/bash
            
            PROJECT_DIR="/storage/emulated/0/Documents/prime-scale-app"
            REMOTE_NAME="gdrive"
            REMOTE_PATH="prime-scale-backup"
            
            rclone sync "$PROJECT_DIR" "$REMOTE_NAME:$REMOTE_PATH" --progress --delete-during
            
            echo "✔ Backup complete: $PROJECT_DIR → $REMOTE_NAME:$REMOTE_PATH"
            ```
            
            ---
            
            ## 2. Restore Script
            
            **File:** `restore_from_drive.sh`
            
            ```bash
            #!/data/data/com.termux/files/usr/bin/bash
            
            PROJECT_DIR="/storage/emulated/0/Documents/prime-scale-app"
            REMOTE_NAME="gdrive"
            REMOTE_PATH="prime-scale-backup"
            
            rclone sync "$REMOTE_NAME:$REMOTE_PATH" "$PROJECT_DIR" --progress --delete-during
            
            echo "✔ Restore complete: $REMOTE_NAME:$REMOTE_PATH → $PROJECT_DIR"
            ```
            
            ---
            
            ## How to Use
            
            Make each script executable:
            ```bash
            chmod +x backup_to_drive.sh
            chmod +x restore_from_drive.sh
            ```
            
            Run backup:
            ```bash
            ./backup_to_drive.sh
            ```
            
            Run restore:
            ```bash
            ./restore_from_drive.sh
            ```
            
            Ensure you have `rclone` installed and configured with a remote named `gdrive`.
            ```

        `script_prompt.py`
        ```py
        """
        Prime Scale App – CLI Entry Point
        
        Usage (run from project root):
          python -m scripts.main --scale-type terrain ...
          python -m scripts.main --scale-type gap ...
          python -m scripts.main --scale-type pure ...
        """
        #comment hashes are used to toggle between different implementations
        import argparse
        #from scripts.core_terrain_scale import generate_terrain_scale
        from scripts.gap_threshold_scout import scan_thresholds
        from scripts.core_pure_prime_scale import generate_pure_prime_scale
        from scripts.core_terrain_scale_modified import generate_terrain_scale
        
        def main():
            parser = argparse.ArgumentParser(description="Prime Scale Generator CLI")
            subparsers = parser.add_subparsers(dest="scale_type", required=True, help="Scale type to generate")
        
            # Terrain scale CLI
            terrain_parser = subparsers.add_parser("terrain", help="Generate terrain-based scale")
            terrain_parser.add_argument("--prime-count", type=int, default=1000)
            terrain_parser.add_argument("--base-frequency", type=float, default=220.0)
            terrain_parser.add_argument("--num-notes", type=int, default=8)
            terrain_parser.add_argument("--window-size", type=float, default=0.007)
            terrain_parser.add_argument("--density-resolution", type=int, default=4000)
            terrain_parser.add_argument("--mode", choices=["valley", "peak"], default="valley")
            terrain_parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
            terrain_parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
            terrain_parser.add_argument("--weight-curve", type=float, default=1.0)
            terrain_parser.set_defaults(include_bounds=True)
        
            # Gap scale CLI
            gap_parser = subparsers.add_parser("gap", help="Generate gap-based scale")
            gap_parser.add_argument("--prime-count", type=int, required=True)
            gap_parser.add_argument("--base-frequency", type=float, default=220.0)
            gap_parser.add_argument("--threshold-range", nargs=2, type=float, required=True, metavar=("MIN", "MAX"))
            gap_parser.add_argument("--step-size", type=float, default=0.001)
            gap_parser.add_argument("--note-goal", type=int, required=True)
            gap_parser.add_argument("--tolerance", type=int, default=1)
            gap_parser.add_argument("--density-resolution", type=int, default=4000)
            gap_parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
            gap_parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
            gap_parser.set_defaults(include_bounds=True)
        
            # Pure scale CLI
            pure_parser = subparsers.add_parser("pure", help="Generate raw prime scale")
            pure_parser.add_argument("--prime-count", type=int, required=True)
            pure_parser.add_argument("--base-frequency", type=float, default=220.0)
            pure_parser.add_argument("--density-resolution", type=int, default=4000)
            pure_parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
            pure_parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
            pure_parser.set_defaults(include_bounds=True)
        
            args = parser.parse_args()
        
            if args.scale_type == "terrain":
                generate_terrain_scale(
                    prime_count=args.prime_count,
                    base_frequency=args.base_frequency,
                    num_notes=args.num_notes,
                    window_size=args.window_size,
                    density_resolution=args.density_resolution,
                    mode=args.mode,
                    include_bounds=args.include_bounds,
                    weight_curve=args.weight_curve
                )
        
            elif args.scale_type == "gap":
                scan_thresholds(
                    prime_count=args.prime_count,
                    threshold_min=args.threshold_range[0],
                    threshold_max=args.threshold_range[1],
                    step_size=args.step_size,
                    note_goal=args.note_goal,
                    tolerance=args.tolerance,
                    base_frequency=args.base_frequency,
                    include_bounds=args.include_bounds,
                    density_resolution=args.density_resolution
                )
        
            elif args.scale_type == "pure":
                generate_pure_prime_scale(
                    prime_count=args.prime_count,
                    base_frequency=args.base_frequency,
                    include_bounds=args.include_bounds,
                    density_resolution=args.density_resolution
                )
        
        if __name__ == "__main__":
            main()
        ```

        **scripts/**

            `scripts/__init__.py`
            ```py
            ```

            **scripts/__pycache__/**

            `scripts/architecture_snapshot.md`
            ```md
            # Project Architecture Snapshot
            
            ## Directory Tree
            
            **.** _(Full Path: `/home/mint/prime-scale-html-viewer/scripts`)_
            
            ├── `__init__.py`
            ├── **__pycache__/**
            │   ├── `__init__.cpython-310.pyc`
            │   ├── `core_pure_prime_scale.cpython-310.pyc`
            │   ├── `core_terrain_scale.cpython-310.pyc`
            │   ├── `core_terrain_scale_modified.cpython-310.pyc`
            │   ├── `gap_threshold_scout.cpython-310.pyc`
            │   ├── `main.cpython-310.pyc`
            │   └── `scale_utils.cpython-310.pyc`
            ├── `architecture_snapshot.md`
            ├── `binary_gap_analyzer.py`
            ├── `cluster_finder.py`
            ├── `core_pure_prime_scale.py`
            ├── `core_terrain_scale.py`
            ├── `core_terrain_scale_final.py`
            ├── `core_terrain_scale_modified.py`
            ├── `gap_threshold_scout.py`
            ├── `main.py`
            └── `scale_utils.py`
            
            ---
            
            ## Project Architecture Snapshot
            
            **/home/mint/prime-scale-html-viewer/scripts**
            
                    `__init__.py`
                    ```py
                    ```
            
                    **__pycache__/**
            
                    `architecture_snapshot.md`
                    ```md
                    # Project Architecture Snapshot
                    
                    ## Directory Tree
                    
                    **.** _(Full Path: `/home/mint/prime-scale-html-viewer/scripts`)_
                    
                    ├── `__init__.py`
                    ├── `binary_gap_analyzer.py`
                    ├── `cluster_finder.py`
                    ├── `core_pure_prime_scale.py`
                    ├── `core_terrain_scale.py`
                    ├── `gap_threshold_scout.py`
                    ├── `main.py`
                    └── `scale_utils.py`
                    
                    ---
                    
                    ## Project Architecture Snapshot
                    
                    **/home/mint/prime-scale-html-viewer/scripts**
                    
                            `__init__.py`
                            ```py
                            ```
                    
                            `binary_gap_analyzer.py`
                            ```py
                            import math
                            
                            def reduce_value(x):
                                while x >= 2:
                                    x /= 2
                                return x
                            
                            def generate_primes(n):
                                primes = []
                                candidate = 2
                                while candidate <= n:
                                    is_prime = True
                                    for p in primes:
                                        if p * p > candidate:
                                            break
                                        if candidate % p == 0:
                                            is_prime = False
                                            break
                                    if is_prime:
                                        primes.append(candidate)
                                    candidate += 1
                                return primes
                            
                            def compute_reduced_primes(tier):
                                primes = generate_primes(tier)
                                reduced = [reduce_value(p) for p in primes]
                                return sorted(reduced), primes
                            
                            def compute_segment_gaps(reduced, tier):
                                segment_width = 1 / (tier // 2)
                                segments = []
                                for i in range(len(reduced) - 1):
                                    start = reduced[i]
                                    end = reduced[i + 1]
                                    gap = end - start
                                    segment_count = round(gap / segment_width)
                                    segments.append((start, end, segment_count))
                                return segments, segment_width
                            ```
                    
                            `cluster_finder.py`
                            ```py
                            import argparse
                            from scripts.binary_gap_analyzer import compute_reduced_primes, compute_segment_gaps
                            import math
                            
                            def log_center(start, end):
                                return math.sqrt(start * end)
                            
                            def find_clusters(segments, threshold=4):
                                clusters = []
                                current_cluster = []
                                for start, end, count in segments:
                                    if count >= threshold:
                                        if current_cluster:
                                            clusters.append(current_cluster)
                                            current_cluster = []
                                    else:
                                        current_cluster.append((start, end))
                                if current_cluster:
                                    clusters.append(current_cluster)
                                return clusters
                            
                            def main():
                                parser = argparse.ArgumentParser(description="Cluster Finder based on segment gaps.")
                                parser.add_argument("--tier", type=int, required=True, help="Binary segmentation tier (must be power of two)")
                                args = parser.parse_args()
                            
                                reduced, _ = compute_reduced_primes(args.tier)
                                segment_data, segment_width = compute_segment_gaps(reduced, args.tier)
                            
                                clusters = find_clusters(segment_data)
                            
                                print(f"Tier: {args.tier} | Segment Width: {segment_width:.6f}")
                                print(f"Found {len(clusters)} cluster(s):\n")
                            
                                for idx, cluster in enumerate(clusters):
                                    cluster_start = cluster[0][0]
                                    cluster_end = cluster[-1][1]
                                    center = log_center(cluster_start, cluster_end)
                                    print(f"Cluster {idx + 1}:")
                                    print(f"  Range: {cluster_start:.6f} -> {cluster_end:.6f}")
                                    print(f"  Log Center: {center:.6f}")
                                    print(f"  Members: {len(cluster)} segments\n")
                            
                            if __name__ == "__main__":
                                main()
                            ```
                    
                            `core_pure_prime_scale.py`
                            ```py
                            import argparse
                            import math
                            from scripts.scale_utils import (
                                generate_primes,
                                get_log_positions,
                                add_bounds,
                                export_json,
                                generate_density_axis  # included for compatibility and visualization
                            )
                            
                            def generate_pure_prime_scale(prime_count, base_frequency, include_bounds=True, density_resolution=4000):
                                primes = generate_primes(prime_count)
                                log_positions = get_log_positions(primes)
                            
                                # Optional: generate axis for any future visualization
                                _ = generate_density_axis(density_resolution)
                            
                                notes = []
                                for log_pos in log_positions:
                                    freq = base_frequency * (2 ** log_pos)
                                    notes.append({
                                        "log_position": log_pos,
                                        "frequency": freq,
                                        "midi": round(69 + 12 * math.log2(freq / 440.0)),
                                        "cents_from_base": 1200 * log_pos,
                                        "prime_sources": []
                                    })
                            
                                if include_bounds:
                                    notes = add_bounds(notes, base_frequency)
                            
                                scale_data = {
                                    "name": f"pure_prime_scale_{prime_count}_primes",
                                    "base_frequency": base_frequency,
                                    "notes": notes
                                }
                            
                                export_json(scale_data, f"pure_prime_scale_{prime_count}_primes.json")
                            
                            if __name__ == "__main__":
                                parser = argparse.ArgumentParser()
                                parser.add_argument("--prime-count", type=int, required=True)
                                parser.add_argument("--base-frequency", type=float, default=220.0)
                                parser.add_argument("--density-resolution", type=int, default=4000)
                                parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
                                parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
                                parser.set_defaults(include_bounds=True)
                            
                                args = parser.parse_args()
                            
                                generate_pure_prime_scale(
                                    prime_count=args.prime_count,
                                    base_frequency=args.base_frequency,
                                    include_bounds=args.include_bounds,
                                    density_resolution=args.density_resolution
                                )
                            ```
                    
                            `core_terrain_scale.py`
                            ```py
                            import argparse
                            import math
                            from scripts.scale_utils import (
                                generate_primes,
                                get_log_positions,
                                prime_weight,
                                circular_distance,
                                generate_density_axis,
                                add_bounds,
                                export_json
                            )
                            
                            # Terrain-specific smoothing function
                            def gravitational_fade(d, w, n=2.5):
                                relative = d / (w / 2)
                                return 1 / (1 + (relative ** n))
                            
                            # Generate density map across log2-reduced space
                            def generate_density_map(log_positions, weights, resolution, window_size):
                                x_axis = generate_density_axis(resolution)
                                density_map = []
                            
                                for x in x_axis:
                                    total_weight = 0
                                    for log_pos, weight in zip(log_positions, weights):
                                        distance = circular_distance(log_pos, x)
                                        if distance <= window_size / 2:
                                            focus = gravitational_fade(distance, window_size)
                                            total_weight += weight * focus
                                    density_map.append(total_weight)
                            
                                return x_axis, density_map
                            
                            # Segment and select notes from density map
                            def select_notes_from_density(x_axis, density_map, num_notes, base_frequency, mode):
                                segment_width = 1.0 / num_notes
                                selected_notes = []
                            
                                for i in range(num_notes):
                                    segment_start = i * segment_width
                                    segment_end = segment_start + segment_width
                                    segment_range = [(x, d) for x, d in zip(x_axis, density_map) if segment_start <= x < segment_end]
                            
                                    if segment_range:
                                        best_x, _ = min(segment_range, key=lambda t: t[1]) if mode == "valley" else max(segment_range, key=lambda t: t[1])
                                        freq = base_frequency * (2 ** best_x)
                                        selected_notes.append({
                                            "log_position": best_x,
                                            "frequency": freq,
                                            "midi": round(69 + 12 * math.log2(freq / 440.0)),
                                            "cents_from_base": 1200 * best_x,
                                            "prime_sources": []
                                        })
                            
                                return selected_notes
                            
                            # Full generator function
                            def generate_terrain_scale(prime_count, base_frequency, num_notes, window_size, density_resolution, mode, include_bounds=True, weight_curve=1.0):
                                primes = generate_primes(prime_count)
                                log_positions = get_log_positions(primes)
                                weights = [prime_weight(p, weight_curve) for p in primes]
                            
                                x_axis, density_map = generate_density_map(log_positions, weights, density_resolution, window_size)
                                selected_notes = select_notes_from_density(x_axis, density_map, num_notes, base_frequency, mode)
                            
                                if include_bounds:
                                    selected_notes = add_bounds(selected_notes, base_frequency)
                            
                                scale_data = {
                                    "name": f"terrain_scale_{num_notes}_{mode}",
                                    "base_frequency": base_frequency,
                                    "notes": selected_notes
                                }
                            
                                filename = f"output/terrain_scale_{num_notes}_{mode}.json"
                                export_json(scale_data, filename)
                            
                            # CLI runner
                            if __name__ == "__main__":
                                parser = argparse.ArgumentParser()
                                parser.add_argument("--prime-count", type=int, default=1000)
                                parser.add_argument("--base-frequency", type=float, default=220.0)
                                parser.add_argument("--num-notes", type=int, default=8)
                                parser.add_argument("--window-size", type=float, default=0.007)
                                parser.add_argument("--density-resolution", type=int, default=4000)
                                parser.add_argument("--mode", choices=["valley", "peak"], default="valley")
                                parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
                                parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
                                parser.add_argument("--weight-curve", type=float, default=1.0)
                                parser.set_defaults(include_bounds=True)
                            
                                args = parser.parse_args()
                            
                                generate_terrain_scale(
                                    prime_count=args.prime_count,
                                    base_frequency=args.base_frequency,
                                    num_notes=args.num_notes,
                                    window_size=args.window_size,
                                    density_resolution=args.density_resolution,
                                    mode=args.mode,
                                    include_bounds=args.include_bounds,
                                    weight_curve=args.weight_curve
                                )
                            ```
                    
                            `gap_threshold_scout.py`
                            ```py
                            import argparse
                            import math
                            from scripts.scale_utils import (
                                generate_primes,
                                get_log_positions,
                                add_bounds,
                                export_json,
                                generate_density_axis  # included for compatibility or plotting if needed
                            )
                            
                            # Count qualifying gaps for a given threshold
                            def detect_gap_count(log_positions, threshold):
                                log_positions.sort()
                                gap_centers = []
                            
                                for i in range(len(log_positions) - 1):
                                    gap = log_positions[i + 1] - log_positions[i]
                                    if gap >= threshold:
                                        center_log = (log_positions[i] + log_positions[i + 1]) / 2
                                        gap_centers.append(center_log)
                            
                                return gap_centers
                            
                            # Scan thresholds to find ones that match note goal
                            def scan_thresholds(prime_count, threshold_min, threshold_max, step_size, note_goal, tolerance, base_frequency, include_bounds, density_resolution):
                                primes = generate_primes(prime_count)
                                log_positions = get_log_positions(primes)
                                matches = []
                            
                                # Optional: could use this for visual overlays or precision matching later
                                _ = generate_density_axis(density_resolution)
                            
                                current = threshold_min
                                while current <= threshold_max:
                                    gap_centers = detect_gap_count(log_positions, current)
                                    count = len(gap_centers)
                            
                                    if abs(count - note_goal) <= tolerance:
                                        print(f"✔ Match: {count} notes at threshold {current:.6f}")
                                        matches.append((current, count, gap_centers))
                                    else:
                                        print(f"... Skipped: {count} notes at threshold {current:.6f}")
                            
                                    current = round(current + step_size, 10)  # Avoid float rounding errors
                            
                                if matches:
                                    best_thresh, best_count, best_centers = matches[0]
                                    notes = []
                                    for log_pos in best_centers:
                                        freq = base_frequency * (2 ** log_pos)
                                        notes.append({
                                            "log_position": log_pos,
                                            "frequency": freq,
                                            "midi": round(69 + 12 * math.log2(freq / 440.0)),
                                            "cents_from_base": 1200 * log_pos,
                                            "prime_sources": []
                                        })
                            
                                    if include_bounds:
                                        notes = add_bounds(notes, base_frequency)
                            
                                    scale_data = {
                                        "name": f"gap_scout_match_{best_count}_notes",
                                        "base_frequency": base_frequency,
                                        "notes": notes
                                    }
                            
                                    export_json(scale_data, f"gap_scout_match_{best_count}_notes.json")
                                else:
                                    print("No matching thresholds found within specified range.")
                            
                            if __name__ == "__main__":
                                parser = argparse.ArgumentParser()
                                parser.add_argument("--prime-count", type=int, required=True)
                                parser.add_argument("--base-frequency", type=float, default=220.0)
                                parser.add_argument("--threshold-range", nargs=2, type=float, required=True, metavar=("MIN", "MAX"))
                                parser.add_argument("--step-size", type=float, default=0.001)
                                parser.add_argument("--note-goal", type=int, required=True)
                                parser.add_argument("--tolerance", type=int, default=1)
                                parser.add_argument("--density-resolution", type=int, default=4000)
                                parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
                                parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
                                parser.set_defaults(include_bounds=True)
                            
                                args = parser.parse_args()
                            
                                scan_thresholds(
                                    prime_count=args.prime_count,
                                    threshold_min=args.threshold_range[0],
                                    threshold_max=args.threshold_range[1],
                                    step_size=args.step_size,
                                    note_goal=args.note_goal,
                                    tolerance=args.tolerance,
                                    base_frequency=args.base_frequency,
                                    include_bounds=args.include_bounds,
                                    density_resolution=args.density_resolution
                                )
                            ```
                    
                            `main.py`
                            ```py
                            """
                            Prime Scale App – CLI Entry Point
                            
                            Usage (run from project root):
                              python -m scripts.main --scale-type terrain ...
                              python -m scripts.main --scale-type gap ...
                              python -m scripts.main --scale-type pure ...
                            """
                            
                            import argparse
                            from scripts.core_terrain_scale import generate_terrain_scale
                            from scripts.gap_threshold_scout import scan_thresholds
                            from scripts.core_pure_prime_scale import generate_pure_prime_scale
                            
                            def main():
                                parser = argparse.ArgumentParser(description="Prime Scale Generator CLI")
                                subparsers = parser.add_subparsers(dest="scale_type", required=True, help="Scale type to generate")
                            
                                # Terrain scale CLI
                                terrain_parser = subparsers.add_parser("terrain", help="Generate terrain-based scale")
                                terrain_parser.add_argument("--prime-count", type=int, default=1000)
                                terrain_parser.add_argument("--base-frequency", type=float, default=220.0)
                                terrain_parser.add_argument("--num-notes", type=int, default=8)
                                terrain_parser.add_argument("--window-size", type=float, default=0.007)
                                terrain_parser.add_argument("--density-resolution", type=int, default=4000)
                                terrain_parser.add_argument("--mode", choices=["valley", "peak"], default="valley")
                                terrain_parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
                                terrain_parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
                                terrain_parser.add_argument("--weight-curve", type=float, default=1.0)
                                terrain_parser.set_defaults(include_bounds=True)
                            
                                # Gap scale CLI
                                gap_parser = subparsers.add_parser("gap", help="Generate gap-based scale")
                                gap_parser.add_argument("--prime-count", type=int, required=True)
                                gap_parser.add_argument("--base-frequency", type=float, default=220.0)
                                gap_parser.add_argument("--threshold-range", nargs=2, type=float, required=True, metavar=("MIN", "MAX"))
                                gap_parser.add_argument("--step-size", type=float, default=0.001)
                                gap_parser.add_argument("--note-goal", type=int, required=True)
                                gap_parser.add_argument("--tolerance", type=int, default=1)
                                gap_parser.add_argument("--density-resolution", type=int, default=4000)
                                gap_parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
                                gap_parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
                                gap_parser.set_defaults(include_bounds=True)
                            
                                # Pure scale CLI
                                pure_parser = subparsers.add_parser("pure", help="Generate raw prime scale")
                                pure_parser.add_argument("--prime-count", type=int, required=True)
                                pure_parser.add_argument("--base-frequency", type=float, default=220.0)
                                pure_parser.add_argument("--density-resolution", type=int, default=4000)
                                pure_parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
                                pure_parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
                                pure_parser.set_defaults(include_bounds=True)
                            
                                args = parser.parse_args()
                            
                                if args.scale_type == "terrain":
                                    generate_terrain_scale(
                                        prime_count=args.prime_count,
                                        base_frequency=args.base_frequency,
                                        num_notes=args.num_notes,
                                        window_size=args.window_size,
                                        density_resolution=args.density_resolution,
                                        mode=args.mode,
                                        include_bounds=args.include_bounds,
                                        weight_curve=args.weight_curve
                                    )
                            
                                elif args.scale_type == "gap":
                                    scan_thresholds(
                                        prime_count=args.prime_count,
                                        threshold_min=args.threshold_range[0],
                                        threshold_max=args.threshold_range[1],
                                        step_size=args.step_size,
                                        note_goal=args.note_goal,
                                        tolerance=args.tolerance,
                                        base_frequency=args.base_frequency,
                                        include_bounds=args.include_bounds,
                                        density_resolution=args.density_resolution
                                    )
                            
                                elif args.scale_type == "pure":
                                    generate_pure_prime_scale(
                                        prime_count=args.prime_count,
                                        base_frequency=args.base_frequency,
                                        include_bounds=args.include_bounds,
                                        density_resolution=args.density_resolution
                                    )
                            
                            if __name__ == "__main__":
                                main()
                            ```
                    
                            `scale_utils.py`
                            ```py
                            import math
                            import json
                            import os
                            
                            def generate_primes(n):
                                primes = [2]
                                candidate = 3
                                while len(primes) < n:
                                    is_prime = True
                                    for p in primes:
                                        if candidate % p == 0:
                                            is_prime = False
                                            break
                                        if p * p > candidate:
                                            break
                                    if is_prime:
                                        primes.append(candidate)
                                    candidate += 2
                                return primes
                            
                            def reduce_value(val):
                                while val >= 2:
                                    val /= 2
                                while val < 1:
                                    val *= 2
                                return val
                            
                            def get_log_positions(primes):
                                """Return log2 positions of primes reduced to the 1–2 octave range."""
                                return [math.log2(reduce_value(p)) for p in primes]
                            
                            def generate_density_axis(resolution):
                                """Returns evenly spaced samples from 0 to 1 (not inclusive) for log-space rendering."""
                                return [i / resolution for i in range(resolution)]
                            
                            def circular_distance(a, b):
                                return min(abs(a - b), 1 - abs(a - b))
                            
                            def prime_weight(p, curve=1.0):
                                if curve == 0.0:
                                    return 1.0
                                return 1 / (p ** curve)
                            
                            def add_bounds(notes, base_freq):
                                bounds = [
                                    {
                                        "log_position": 0.0,
                                        "frequency": base_freq,
                                        "midi": round(69 + 12 * math.log2(base_freq / 440.0)),
                                        "cents_from_base": 0.0,
                                        "prime_sources": []
                                    },
                                    {
                                        "log_position": 1.0,
                                        "frequency": base_freq * 2,
                                        "midi": round(69 + 12 * math.log2((base_freq * 2) / 440.0)),
                                        "cents_from_base": 1200.0,
                                        "prime_sources": []
                                    }
                                ]
                                return [bounds[0]] + notes + [bounds[1]]
                            
                            def export_json(scale_data, filename):
                                # Always write to top-level /output/ folder
                                script_dir = os.path.dirname(os.path.abspath(__file__))
                                project_root = os.path.dirname(script_dir)
                                output_dir = os.path.join(project_root, "output")
                            
                                os.makedirs(output_dir, exist_ok=True)
                                full_path = os.path.join(output_dir, os.path.basename(filename))
                            
                                with open(full_path, "w", encoding="utf-8") as f:
                                    json.dump(scale_data, f, indent=2)
                            
                                print(f"✔ Saved scale to {full_path}")
                            ```
                    ```
            
                    `binary_gap_analyzer.py`
                    ```py
                    import math
                    
                    def reduce_value(x):
                        while x >= 2:
                            x /= 2
                        return x
                    
                    def generate_primes(n):
                        primes = []
                        candidate = 2
                        while candidate <= n:
                            is_prime = True
                            for p in primes:
                                if p * p > candidate:
                                    break
                                if candidate % p == 0:
                                    is_prime = False
                                    break
                            if is_prime:
                                primes.append(candidate)
                            candidate += 1
                        return primes
                    
                    def compute_reduced_primes(tier):
                        primes = generate_primes(tier)
                        reduced = [reduce_value(p) for p in primes]
                        return sorted(reduced), primes
                    
                    def compute_segment_gaps(reduced, tier):
                        segment_width = 1 / (tier // 2)
                        segments = []
                        for i in range(len(reduced) - 1):
                            start = reduced[i]
                            end = reduced[i + 1]
                            gap = end - start
                            segment_count = round(gap / segment_width)
                            segments.append((start, end, segment_count))
                        return segments, segment_width
                    ```
            
                    `cluster_finder.py`
                    ```py
                    import argparse
                    from scripts.binary_gap_analyzer import compute_reduced_primes, compute_segment_gaps
                    import math
                    
                    def log_center(start, end):
                        return math.sqrt(start * end)
                    
                    def find_clusters(segments, threshold=4):
                        clusters = []
                        current_cluster = []
                        for start, end, count in segments:
                            if count >= threshold:
                                if current_cluster:
                                    clusters.append(current_cluster)
                                    current_cluster = []
                            else:
                                current_cluster.append((start, end))
                        if current_cluster:
                            clusters.append(current_cluster)
                        return clusters
                    
                    def main():
                        parser = argparse.ArgumentParser(description="Cluster Finder based on segment gaps.")
                        parser.add_argument("--tier", type=int, required=True, help="Binary segmentation tier (must be power of two)")
                        args = parser.parse_args()
                    
                        reduced, _ = compute_reduced_primes(args.tier)
                        segment_data, segment_width = compute_segment_gaps(reduced, args.tier)
                    
                        clusters = find_clusters(segment_data)
                    
                        print(f"Tier: {args.tier} | Segment Width: {segment_width:.6f}")
                        print(f"Found {len(clusters)} cluster(s):\n")
                    
                        for idx, cluster in enumerate(clusters):
                            cluster_start = cluster[0][0]
                            cluster_end = cluster[-1][1]
                            center = log_center(cluster_start, cluster_end)
                            print(f"Cluster {idx + 1}:")
                            print(f"  Range: {cluster_start:.6f} -> {cluster_end:.6f}")
                            print(f"  Log Center: {center:.6f}")
                            print(f"  Members: {len(cluster)} segments\n")
                    
                    if __name__ == "__main__":
                        main()
                    ```
            
                    `core_pure_prime_scale.py`
                    ```py
                    import argparse
                    import math
                    from scripts.scale_utils import (
                        generate_primes,
                        get_log_positions,
                        add_bounds,
                        export_json,
                        generate_density_axis  # included for compatibility and visualization
                    )
                    
                    def generate_pure_prime_scale(prime_count, base_frequency, include_bounds=True, density_resolution=4000):
                        primes = generate_primes(prime_count)
                        log_positions = get_log_positions(primes)
                    
                        # Optional: generate axis for any future visualization
                        _ = generate_density_axis(density_resolution)
                    
                        notes = []
                        for log_pos in log_positions:
                            freq = base_frequency * (2 ** log_pos)
                            notes.append({
                                "log_position": log_pos,
                                "frequency": freq,
                                "midi": round(69 + 12 * math.log2(freq / 440.0)),
                                "cents_from_base": 1200 * log_pos,
                                "prime_sources": []
                            })
                    
                        if include_bounds:
                            notes = add_bounds(notes, base_frequency)
                    
                        scale_data = {
                            "name": f"pure_prime_scale_{prime_count}_primes",
                            "base_frequency": base_frequency,
                            "notes": notes
                        }
                    
                        export_json(scale_data, f"pure_prime_scale_{prime_count}_primes.json")
                    
                    if __name__ == "__main__":
                        parser = argparse.ArgumentParser()
                        parser.add_argument("--prime-count", type=int, required=True)
                        parser.add_argument("--base-frequency", type=float, default=220.0)
                        parser.add_argument("--density-resolution", type=int, default=4000)
                        parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
                        parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
                        parser.set_defaults(include_bounds=True)
                    
                        args = parser.parse_args()
                    
                        generate_pure_prime_scale(
                            prime_count=args.prime_count,
                            base_frequency=args.base_frequency,
                            include_bounds=args.include_bounds,
                            density_resolution=args.density_resolution
                        )
                    ```
            
                    `core_terrain_scale.py`
                    ```py
                    import argparse
                    import math
                    from scripts.scale_utils import (
                        generate_primes,
                        get_log_positions,
                        prime_weight,
                        circular_distance,
                        generate_density_axis,
                        add_bounds,
                        export_json
                    )
                    
                    # Terrain-specific smoothing function
                    def gravitational_fade(d, w, n=2.5):
                        relative = d / (w / 2)
                        return 1 / (1 + (relative ** n))
                    
                    # Generate density map across log2-reduced space
                    def generate_density_map(log_positions, weights, resolution, window_size):
                        x_axis = generate_density_axis(resolution)
                        density_map = []
                    
                        for x in x_axis:
                            total_weight = 0
                            for log_pos, weight in zip(log_positions, weights):
                                distance = circular_distance(log_pos, x)
                                if distance <= window_size / 2:
                                    focus = gravitational_fade(distance, window_size)
                                    total_weight += weight * focus
                            density_map.append(total_weight)
                    
                        return x_axis, density_map
                    
                    # Segment and select notes from density map
                    def select_notes_from_density(x_axis, density_map, num_notes, base_frequency, mode):
                        segment_width = 1.0 / num_notes
                        selected_notes = []
                    
                        for i in range(num_notes):
                            segment_start = i * segment_width
                            segment_end = segment_start + segment_width
                            segment_range = [(x, d) for x, d in zip(x_axis, density_map) if segment_start <= x < segment_end]
                    
                            if segment_range:
                                best_x, _ = min(segment_range, key=lambda t: t[1]) if mode == "valley" else max(segment_range, key=lambda t: t[1])
                                freq = base_frequency * (2 ** best_x)
                                selected_notes.append({
                                    "log_position": best_x,
                                    "frequency": freq,
                                    "midi": round(69 + 12 * math.log2(freq / 440.0)),
                                    "cents_from_base": 1200 * best_x,
                                    "prime_sources": []
                                })
                    
                        return selected_notes
                    
                    # Full generator function
                    def generate_terrain_scale(prime_count, base_frequency, num_notes, window_size, density_resolution, mode, include_bounds=True, weight_curve=1.0):
                        primes = generate_primes(prime_count)
                        log_positions = get_log_positions(primes)
                        weights = [prime_weight(p, weight_curve) for p in primes]
                    
                        x_axis, density_map = generate_density_map(log_positions, weights, density_resolution, window_size)
                        selected_notes = select_notes_from_density(x_axis, density_map, num_notes, base_frequency, mode)
                    
                        if include_bounds:
                            selected_notes = add_bounds(selected_notes, base_frequency)
                    
                        scale_data = {
                            "name": f"terrain_scale_{num_notes}_{mode}",
                            "base_frequency": base_frequency,
                            "notes": selected_notes
                        }
                    
                        filename = f"output/terrain_scale_{num_notes}_{mode}.json"
                        export_json(scale_data, filename)
                    
                    # CLI runner
                    if __name__ == "__main__":
                        parser = argparse.ArgumentParser()
                        parser.add_argument("--prime-count", type=int, default=1000)
                        parser.add_argument("--base-frequency", type=float, default=220.0)
                        parser.add_argument("--num-notes", type=int, default=8)
                        parser.add_argument("--window-size", type=float, default=0.007)
                        parser.add_argument("--density-resolution", type=int, default=4000)
                        parser.add_argument("--mode", choices=["valley", "peak"], default="valley")
                        parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
                        parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
                        parser.add_argument("--weight-curve", type=float, default=1.0)
                        parser.set_defaults(include_bounds=True)
                    
                        args = parser.parse_args()
                    
                        generate_terrain_scale(
                            prime_count=args.prime_count,
                            base_frequency=args.base_frequency,
                            num_notes=args.num_notes,
                            window_size=args.window_size,
                            density_resolution=args.density_resolution,
                            mode=args.mode,
                            include_bounds=args.include_bounds,
                            weight_curve=args.weight_curve
                        )
                    ```
            
                    `core_terrain_scale_final.py`
                    ```py
                    # ===[ IMPORTS & CONSTANTS ]===
                    import argparse
                    import json
                    import math
                    import os
                    
                    # ===[ PRIME UTILITIES ]===
                    def generate_primes(n):
                        primes = [2]
                        candidate = 3
                        while len(primes) < n:
                            is_prime = True
                            for p in primes:
                                if candidate % p == 0:
                                    is_prime = False
                                    break
                                if p * p > candidate:
                                    break
                            if is_prime:
                                primes.append(candidate)
                            candidate += 2
                        return primes
                    
                    def reduce_value(val):
                        while val >= 2:
                            val /= 2
                        while val < 1:
                            val *= 2
                        return val
                    
                    # ===[ DENSITY LENS PROFILE ]===
                    def gravitational_fade(d, w, n=2.5):
                        relative = d / (w / 2)
                        return 1 / (1 + (relative ** n))
                    
                    # ===[ MAIN SCALE GENERATION ENGINE ]===
                    def generate_scale(prime_count, base_frequency, num_notes, window_size, density_resolution, mode):
                        primes = generate_primes(prime_count)
                        print(f"✔ Generated {len(primes)} primes")
                    
                        log_positions = [math.log2(reduce_value(p)) for p in primes]
                        weights = [1 / p for p in primes]
                        print("✔ Prepared log positions and reciprocal weights")
                    
                        x_axis = [i / density_resolution for i in range(density_resolution)]
                        density_map = []
                    
                        for i, x in enumerate(x_axis):
                            if i % (density_resolution // 10) == 0:
                                print(f"  > Density progress: {int(i / density_resolution * 100)}%")
                            total_weight = 0
                            for log_pos, weight in zip(log_positions, weights):
                                distance = abs(log_pos - x)
                                wrapped_distance = min(distance, 1 - distance)
                                if wrapped_distance <= window_size / 2:
                                    focus = gravitational_fade(wrapped_distance, window_size)
                                    total_weight += weight * focus
                            density_map.append(total_weight)
                        print("✔ Completed density mapping")
                    
                        segment_width = 1.0 / num_notes
                        selected_notes = []
                    
                        for i in range(num_notes):
                            segment_start = i * segment_width
                            segment_end = segment_start + segment_width
                            segment_range = [(x, d) for x, d in zip(x_axis, density_map) if segment_start <= x < segment_end]
                            if segment_range:
                                if mode == "valley":
                                    best_x, _ = min(segment_range, key=lambda t: t[1])
                                elif mode == "peak":
                                    best_x, _ = max(segment_range, key=lambda t: t[1])
                                else:
                                    raise ValueError("Invalid mode. Use 'valley' or 'peak'.")
                    
                                frequency = base_frequency * (2 ** best_x)
                                midi_note = round(69 + 12 * math.log2(frequency / 440.0))
                                cents = 1200 * best_x
                    
                                selected_notes.append({
                                    "log_position": best_x,
                                    "frequency": frequency,
                                    "midi": midi_note,
                                    "cents_from_base": cents,
                                    "prime_sources": []
                                })
                        print("✔ Selected all notes and generating output file...")
                    
                        # Prepare extended metadata
                        metadata = {
                            "primes": primes,
                            "prime_count": len(primes),
                            "linear_prime_positions": [reduce_value(p) for p in primes],
                            "log_prime_positions": log_positions,
                            "x_axis": x_axis,
                            "density_map": density_map,
                            "algorithm_manifest": {
                                "name": "core_terrain_scale",
                                "mode": mode,
                                "window_size": window_size,
                                "lens_profile": "gravitational"
                            }
                        }
                    
                        scale_data = {
                            "metadata": metadata,
                            "name": f"terrain_scale_{num_notes}_{mode}",
                            "base_frequency": base_frequency,
                            "notes": selected_notes
                        }
                    
                        filename = os.path.expanduser(f"~/prime-scale-html-viewer/output/terrain_scale_{num_notes}_{mode}.json")
                        with open(filename, "w") as f:
                            json.dump(scale_data, f, indent=2)
                    
                        print(f"✔ Scale saved to {os.path.abspath(filename)}")
                    
                    # ===[ COMMAND LINE ENTRY ]===
                    if __name__ == "__main__":
                        parser = argparse.ArgumentParser(description="Generate a musical scale from prime terrain.")
                        parser.add_argument("--prime-count", type=int, default=1000)
                        parser.add_argument("--base-frequency", type=float, default=220.0)
                        parser.add_argument("--num-notes", type=int, default=8)
                        parser.add_argument("--window-size", type=float, default=0.007)
                        parser.add_argument("--density-resolution", type=int, default=4000)
                        parser.add_argument("--mode", choices=["valley", "peak"], default="valley")
                    
                        args = parser.parse_args()
                        generate_scale(
                            prime_count=args.prime_count,
                            base_frequency=args.base_frequency,
                            num_notes=args.num_notes,
                            window_size=args.window_size,
                            density_resolution=args.density_resolution,
                            mode=args.mode
                        )
                    ```
            
                    `core_terrain_scale_modified.py`
                    ```py
                    import argparse
                    import math
                    from scripts.scale_utils import (
                        generate_primes,
                        get_log_positions,
                        prime_weight,
                        circular_distance,
                        generate_density_axis,
                        add_bounds,
                        export_json
                    )
                    
                    # Terrain-specific smoothing function
                    def gravitational_fade(d, w, n=2.5):
                        relative = d / (w / 2)
                        return 1 / (1 + (relative ** n))
                    
                    # Generate density map across log2-reduced space
                    def generate_density_map(log_positions, weights, resolution, window_size):
                        x_axis = generate_density_axis(resolution)
                        density_map = []
                    
                        for x in x_axis:
                            total_weight = 0
                            for log_pos, weight in zip(log_positions, weights):
                                distance = circular_distance(log_pos, x)
                                if distance <= window_size / 2:
                                    focus = gravitational_fade(distance, window_size)
                                    total_weight += weight * focus
                            density_map.append(total_weight)
                    
                        return x_axis, density_map
                    
                    # Segment and select notes from density map
                    def select_notes_from_density(x_axis, density_map, num_notes, base_frequency, mode):
                        segment_width = 1.0 / num_notes
                        selected_notes = []
                    
                        for i in range(num_notes):
                            segment_start = i * segment_width
                            segment_end = segment_start + segment_width
                            segment_range = [(x, d) for x, d in zip(x_axis, density_map) if segment_start <= x < segment_end]
                    
                            if segment_range:
                                best_x, _ = min(segment_range, key=lambda t: t[1]) if mode == "valley" else max(segment_range, key=lambda t: t[1])
                                freq = base_frequency * (2 ** best_x)
                                selected_notes.append({
                                    "log_position": best_x,
                                    "frequency": freq,
                                    "midi": round(69 + 12 * math.log2(freq / 440.0)),
                                    "cents_from_base": 1200 * best_x,
                                    "prime_sources": []
                                })
                    
                        return selected_notes
                    
                    # Full generator function
                    def generate_terrain_scale(prime_count, base_frequency, num_notes, window_size, density_resolution, mode, include_bounds=True, weight_curve=1.0):
                        primes = generate_primes(prime_count)
                        log_positions = get_log_positions(primes)
                        weights = [prime_weight(p, weight_curve) for p in primes]
                    
                        x_axis, density_map = generate_density_map(log_positions, weights, density_resolution, window_size)
                        selected_notes = select_notes_from_density(x_axis, density_map, num_notes, base_frequency, mode)
                    
                        if include_bounds:
                            selected_notes = add_bounds(selected_notes, base_frequency)
                    
                        scale_data = {
                            "name": f"terrain_scale_{num_notes}_{mode}",
                            "base_frequency": base_frequency,
                            "notes": selected_notes,
                            "log_prime_positions": log_positions,
                            "segment_boundaries": [i / num_notes for i in range(num_notes + 1)]
                        }
                    
                        filename = f"output/terrain_scale_{num_notes}_{mode}.json"
                        export_json(scale_data, filename)
                    
                    # CLI runner
                    if __name__ == "__main__":
                        parser = argparse.ArgumentParser()
                        parser.add_argument("--prime-count", type=int, default=1000)
                        parser.add_argument("--base-frequency", type=float, default=220.0)
                        parser.add_argument("--num-notes", type=int, default=8)
                        parser.add_argument("--window-size", type=float, default=0.007)
                        parser.add_argument("--density-resolution", type=int, default=4000)
                        parser.add_argument("--mode", choices=["valley", "peak"], default="valley")
                        parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
                        parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
                        parser.add_argument("--weight-curve", type=float, default=1.0)
                        parser.set_defaults(include_bounds=True)
                    
                        args = parser.parse_args()
                    
                        generate_terrain_scale(
                            prime_count=args.prime_count,
                            base_frequency=args.base_frequency,
                            num_notes=args.num_notes,
                            window_size=args.window_size,
                            density_resolution=args.density_resolution,
                            mode=args.mode,
                            include_bounds=args.include_bounds,
                            weight_curve=args.weight_curve
                        )
                    ```
            
                    `gap_threshold_scout.py`
                    ```py
                    import argparse
                    import math
                    from scripts.scale_utils import (
                        generate_primes,
                        get_log_positions,
                        add_bounds,
                        export_json,
                        generate_density_axis  # included for compatibility or plotting if needed
                    )
                    
                    # Count qualifying gaps for a given threshold
                    def detect_gap_count(log_positions, threshold):
                        log_positions.sort()
                        gap_centers = []
                    
                        for i in range(len(log_positions) - 1):
                            gap = log_positions[i + 1] - log_positions[i]
                            if gap >= threshold:
                                center_log = (log_positions[i] + log_positions[i + 1]) / 2
                                gap_centers.append(center_log)
                    
                        return gap_centers
                    
                    # Scan thresholds to find ones that match note goal
                    def scan_thresholds(prime_count, threshold_min, threshold_max, step_size, note_goal, tolerance, base_frequency, include_bounds, density_resolution):
                        primes = generate_primes(prime_count)
                        log_positions = get_log_positions(primes)
                        matches = []
                    
                        # Optional: could use this for visual overlays or precision matching later
                        _ = generate_density_axis(density_resolution)
                    
                        current = threshold_min
                        while current <= threshold_max:
                            gap_centers = detect_gap_count(log_positions, current)
                            count = len(gap_centers)
                    
                            if abs(count - note_goal) <= tolerance:
                                print(f"✔ Match: {count} notes at threshold {current:.6f}")
                                matches.append((current, count, gap_centers))
                            else:
                                print(f"... Skipped: {count} notes at threshold {current:.6f}")
                    
                            current = round(current + step_size, 10)  # Avoid float rounding errors
                    
                        if matches:
                            best_thresh, best_count, best_centers = matches[0]
                            notes = []
                            for log_pos in best_centers:
                                freq = base_frequency * (2 ** log_pos)
                                notes.append({
                                    "log_position": log_pos,
                                    "frequency": freq,
                                    "midi": round(69 + 12 * math.log2(freq / 440.0)),
                                    "cents_from_base": 1200 * log_pos,
                                    "prime_sources": []
                                })
                    
                            if include_bounds:
                                notes = add_bounds(notes, base_frequency)
                    
                            scale_data = {
                                "name": f"gap_scout_match_{best_count}_notes",
                                "base_frequency": base_frequency,
                                "notes": notes
                            }
                    
                            export_json(scale_data, f"gap_scout_match_{best_count}_notes.json")
                        else:
                            print("No matching thresholds found within specified range.")
                    
                    if __name__ == "__main__":
                        parser = argparse.ArgumentParser()
                        parser.add_argument("--prime-count", type=int, required=True)
                        parser.add_argument("--base-frequency", type=float, default=220.0)
                        parser.add_argument("--threshold-range", nargs=2, type=float, required=True, metavar=("MIN", "MAX"))
                        parser.add_argument("--step-size", type=float, default=0.001)
                        parser.add_argument("--note-goal", type=int, required=True)
                        parser.add_argument("--tolerance", type=int, default=1)
                        parser.add_argument("--density-resolution", type=int, default=4000)
                        parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
                        parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
                        parser.set_defaults(include_bounds=True)
                    
                        args = parser.parse_args()
                    
                        scan_thresholds(
                            prime_count=args.prime_count,
                            threshold_min=args.threshold_range[0],
                            threshold_max=args.threshold_range[1],
                            step_size=args.step_size,
                            note_goal=args.note_goal,
                            tolerance=args.tolerance,
                            base_frequency=args.base_frequency,
                            include_bounds=args.include_bounds,
                            density_resolution=args.density_resolution
                        )
                    ```
            
                    `main.py`
                    ```py
                    """
                    Prime Scale App – CLI Entry Point
                    
                    Usage (run from project root):
                      python -m scripts.main --scale-type terrain ...
                      python -m scripts.main --scale-type gap ...
                      python -m scripts.main --scale-type pure ...
                    """
                    #comment hashes are used to toggle between different implementations
                    import argparse
                    #from scripts.core_terrain_scale import generate_terrain_scale
                    from scripts.gap_threshold_scout import scan_thresholds
                    from scripts.core_pure_prime_scale import generate_pure_prime_scale
                    from scripts.core_terrain_scale_modified import generate_terrain_scale
                    
                    def main():
                        parser = argparse.ArgumentParser(description="Prime Scale Generator CLI")
                        subparsers = parser.add_subparsers(dest="scale_type", required=True, help="Scale type to generate")
                    
                        # Terrain scale CLI
                        terrain_parser = subparsers.add_parser("terrain", help="Generate terrain-based scale")
                        terrain_parser.add_argument("--prime-count", type=int, default=1000)
                        terrain_parser.add_argument("--base-frequency", type=float, default=220.0)
                        terrain_parser.add_argument("--num-notes", type=int, default=8)
                        terrain_parser.add_argument("--window-size", type=float, default=0.007)
                        terrain_parser.add_argument("--density-resolution", type=int, default=4000)
                        terrain_parser.add_argument("--mode", choices=["valley", "peak"], default="valley")
                        terrain_parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
                        terrain_parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
                        terrain_parser.add_argument("--weight-curve", type=float, default=1.0)
                        terrain_parser.set_defaults(include_bounds=True)
                    
                        # Gap scale CLI
                        gap_parser = subparsers.add_parser("gap", help="Generate gap-based scale")
                        gap_parser.add_argument("--prime-count", type=int, required=True)
                        gap_parser.add_argument("--base-frequency", type=float, default=220.0)
                        gap_parser.add_argument("--threshold-range", nargs=2, type=float, required=True, metavar=("MIN", "MAX"))
                        gap_parser.add_argument("--step-size", type=float, default=0.001)
                        gap_parser.add_argument("--note-goal", type=int, required=True)
                        gap_parser.add_argument("--tolerance", type=int, default=1)
                        gap_parser.add_argument("--density-resolution", type=int, default=4000)
                        gap_parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
                        gap_parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
                        gap_parser.set_defaults(include_bounds=True)
                    
                        # Pure scale CLI
                        pure_parser = subparsers.add_parser("pure", help="Generate raw prime scale")
                        pure_parser.add_argument("--prime-count", type=int, required=True)
                        pure_parser.add_argument("--base-frequency", type=float, default=220.0)
                        pure_parser.add_argument("--density-resolution", type=int, default=4000)
                        pure_parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
                        pure_parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
                        pure_parser.set_defaults(include_bounds=True)
                    
                        args = parser.parse_args()
                    
                        if args.scale_type == "terrain":
                            generate_terrain_scale(
                                prime_count=args.prime_count,
                                base_frequency=args.base_frequency,
                                num_notes=args.num_notes,
                                window_size=args.window_size,
                                density_resolution=args.density_resolution,
                                mode=args.mode,
                                include_bounds=args.include_bounds,
                                weight_curve=args.weight_curve
                            )
                    
                        elif args.scale_type == "gap":
                            scan_thresholds(
                                prime_count=args.prime_count,
                                threshold_min=args.threshold_range[0],
                                threshold_max=args.threshold_range[1],
                                step_size=args.step_size,
                                note_goal=args.note_goal,
                                tolerance=args.tolerance,
                                base_frequency=args.base_frequency,
                                include_bounds=args.include_bounds,
                                density_resolution=args.density_resolution
                            )
                    
                        elif args.scale_type == "pure":
                            generate_pure_prime_scale(
                                prime_count=args.prime_count,
                                base_frequency=args.base_frequency,
                                include_bounds=args.include_bounds,
                                density_resolution=args.density_resolution
                            )
                    
                    if __name__ == "__main__":
                        main()
                    ```
            
                    `scale_utils.py`
                    ```py
                    import math
                    import json
                    import os
                    
                    def generate_primes(n):
                        primes = [2]
                        candidate = 3
                        while len(primes) < n:
                            is_prime = True
                            for p in primes:
                                if candidate % p == 0:
                                    is_prime = False
                                    break
                                if p * p > candidate:
                                    break
                            if is_prime:
                                primes.append(candidate)
                            candidate += 2
                        return primes
                    
                    def reduce_value(val):
                        while val >= 2:
                            val /= 2
                        while val < 1:
                            val *= 2
                        return val
                    
                    def get_log_positions(primes):
                        """Return log2 positions of primes reduced to the 1–2 octave range."""
                        return [math.log2(reduce_value(p)) for p in primes]
                    
                    def generate_density_axis(resolution):
                        """Returns evenly spaced samples from 0 to 1 (not inclusive) for log-space rendering."""
                        return [i / resolution for i in range(resolution)]
                    
                    def circular_distance(a, b):
                        return min(abs(a - b), 1 - abs(a - b))
                    
                    def prime_weight(p, curve=1.0):
                        if curve == 0.0:
                            return 1.0
                        return 1 / (p ** curve)
                    
                    def add_bounds(notes, base_freq):
                        bounds = [
                            {
                                "log_position": 0.0,
                                "frequency": base_freq,
                                "midi": round(69 + 12 * math.log2(base_freq / 440.0)),
                                "cents_from_base": 0.0,
                                "prime_sources": []
                            },
                            {
                                "log_position": 1.0,
                                "frequency": base_freq * 2,
                                "midi": round(69 + 12 * math.log2((base_freq * 2) / 440.0)),
                                "cents_from_base": 1200.0,
                                "prime_sources": []
                            }
                        ]
                        return [bounds[0]] + notes + [bounds[1]]
                    
                    def export_json(scale_data, filename):
                        # Always write to top-level /output/ folder
                        script_dir = os.path.dirname(os.path.abspath(__file__))
                        project_root = os.path.dirname(script_dir)
                        output_dir = os.path.join(project_root, "output")
                    
                        os.makedirs(output_dir, exist_ok=True)
                        full_path = os.path.join(output_dir, os.path.basename(filename))
                    
                        with open(full_path, "w", encoding="utf-8") as f:
                            json.dump(scale_data, f, indent=2)
                    
                        print(f"✔ Saved scale to {full_path}")
                    ```
            ```

            `scripts/binary_gap_analyzer.py`
            ```py
            import math
            
            def reduce_value(x):
                while x >= 2:
                    x /= 2
                return x
            
            def generate_primes(n):
                primes = []
                candidate = 2
                while candidate <= n:
                    is_prime = True
                    for p in primes:
                        if p * p > candidate:
                            break
                        if candidate % p == 0:
                            is_prime = False
                            break
                    if is_prime:
                        primes.append(candidate)
                    candidate += 1
                return primes
            
            def compute_reduced_primes(tier):
                primes = generate_primes(tier)
                reduced = [reduce_value(p) for p in primes]
                return sorted(reduced), primes
            
            def compute_segment_gaps(reduced, tier):
                segment_width = 1 / (tier // 2)
                segments = []
                for i in range(len(reduced) - 1):
                    start = reduced[i]
                    end = reduced[i + 1]
                    gap = end - start
                    segment_count = round(gap / segment_width)
                    segments.append((start, end, segment_count))
                return segments, segment_width
            ```

            `scripts/cluster_finder.py`
            ```py
            import argparse
            from scripts.binary_gap_analyzer import compute_reduced_primes, compute_segment_gaps
            import math
            
            def log_center(start, end):
                return math.sqrt(start * end)
            
            def find_clusters(segments, threshold=4):
                clusters = []
                current_cluster = []
                for start, end, count in segments:
                    if count >= threshold:
                        if current_cluster:
                            clusters.append(current_cluster)
                            current_cluster = []
                    else:
                        current_cluster.append((start, end))
                if current_cluster:
                    clusters.append(current_cluster)
                return clusters
            
            def main():
                parser = argparse.ArgumentParser(description="Cluster Finder based on segment gaps.")
                parser.add_argument("--tier", type=int, required=True, help="Binary segmentation tier (must be power of two)")
                args = parser.parse_args()
            
                reduced, _ = compute_reduced_primes(args.tier)
                segment_data, segment_width = compute_segment_gaps(reduced, args.tier)
            
                clusters = find_clusters(segment_data)
            
                print(f"Tier: {args.tier} | Segment Width: {segment_width:.6f}")
                print(f"Found {len(clusters)} cluster(s):\n")
            
                for idx, cluster in enumerate(clusters):
                    cluster_start = cluster[0][0]
                    cluster_end = cluster[-1][1]
                    center = log_center(cluster_start, cluster_end)
                    print(f"Cluster {idx + 1}:")
                    print(f"  Range: {cluster_start:.6f} -> {cluster_end:.6f}")
                    print(f"  Log Center: {center:.6f}")
                    print(f"  Members: {len(cluster)} segments\n")
            
            if __name__ == "__main__":
                main()
            ```

            `scripts/core_pure_prime_scale.py`
            ```py
            import argparse
            import math
            from scripts.scale_utils import (
                generate_primes,
                get_log_positions,
                add_bounds,
                export_json,
                generate_density_axis  # included for compatibility and visualization
            )
            
            def generate_pure_prime_scale(prime_count, base_frequency, include_bounds=True, density_resolution=4000):
                primes = generate_primes(prime_count)
                log_positions = get_log_positions(primes)
            
                # Optional: generate axis for any future visualization
                _ = generate_density_axis(density_resolution)
            
                notes = []
                for log_pos in log_positions:
                    freq = base_frequency * (2 ** log_pos)
                    notes.append({
                        "log_position": log_pos,
                        "frequency": freq,
                        "midi": round(69 + 12 * math.log2(freq / 440.0)),
                        "cents_from_base": 1200 * log_pos,
                        "prime_sources": []
                    })
            
                if include_bounds:
                    notes = add_bounds(notes, base_frequency)
            
                scale_data = {
                    "name": f"pure_prime_scale_{prime_count}_primes",
                    "base_frequency": base_frequency,
                    "notes": notes
                }
            
                export_json(scale_data, f"pure_prime_scale_{prime_count}_primes.json")
            
            if __name__ == "__main__":
                parser = argparse.ArgumentParser()
                parser.add_argument("--prime-count", type=int, required=True)
                parser.add_argument("--base-frequency", type=float, default=220.0)
                parser.add_argument("--density-resolution", type=int, default=4000)
                parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
                parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
                parser.set_defaults(include_bounds=True)
            
                args = parser.parse_args()
            
                generate_pure_prime_scale(
                    prime_count=args.prime_count,
                    base_frequency=args.base_frequency,
                    include_bounds=args.include_bounds,
                    density_resolution=args.density_resolution
                )
            ```

            `scripts/core_terrain_scale.py`
            ```py
            import argparse
            import math
            from scripts.scale_utils import (
                generate_primes,
                get_log_positions,
                prime_weight,
                circular_distance,
                generate_density_axis,
                add_bounds,
                export_json
            )
            
            # Terrain-specific smoothing function
            def gravitational_fade(d, w, n=2.5):
                relative = d / (w / 2)
                return 1 / (1 + (relative ** n))
            
            # Generate density map across log2-reduced space
            def generate_density_map(log_positions, weights, resolution, window_size):
                x_axis = generate_density_axis(resolution)
                density_map = []
            
                for x in x_axis:
                    total_weight = 0
                    for log_pos, weight in zip(log_positions, weights):
                        distance = circular_distance(log_pos, x)
                        if distance <= window_size / 2:
                            focus = gravitational_fade(distance, window_size)
                            total_weight += weight * focus
                    density_map.append(total_weight)
            
                return x_axis, density_map
            
            # Segment and select notes from density map
            def select_notes_from_density(x_axis, density_map, num_notes, base_frequency, mode):
                segment_width = 1.0 / num_notes
                selected_notes = []
            
                for i in range(num_notes):
                    segment_start = i * segment_width
                    segment_end = segment_start + segment_width
                    segment_range = [(x, d) for x, d in zip(x_axis, density_map) if segment_start <= x < segment_end]
            
                    if segment_range:
                        best_x, _ = min(segment_range, key=lambda t: t[1]) if mode == "valley" else max(segment_range, key=lambda t: t[1])
                        freq = base_frequency * (2 ** best_x)
                        selected_notes.append({
                            "log_position": best_x,
                            "frequency": freq,
                            "midi": round(69 + 12 * math.log2(freq / 440.0)),
                            "cents_from_base": 1200 * best_x,
                            "prime_sources": []
                        })
            
                return selected_notes
            
            # Full generator function
            def generate_terrain_scale(prime_count, base_frequency, num_notes, window_size, density_resolution, mode, include_bounds=True, weight_curve=1.0):
                primes = generate_primes(prime_count)
                log_positions = get_log_positions(primes)
                weights = [prime_weight(p, weight_curve) for p in primes]
            
                x_axis, density_map = generate_density_map(log_positions, weights, density_resolution, window_size)
                selected_notes = select_notes_from_density(x_axis, density_map, num_notes, base_frequency, mode)
            
                if include_bounds:
                    selected_notes = add_bounds(selected_notes, base_frequency)
            
                scale_data = {
                    "name": f"terrain_scale_{num_notes}_{mode}",
                    "base_frequency": base_frequency,
                    "notes": selected_notes
                }
            
                filename = f"output/terrain_scale_{num_notes}_{mode}.json"
                export_json(scale_data, filename)
            
            # CLI runner
            if __name__ == "__main__":
                parser = argparse.ArgumentParser()
                parser.add_argument("--prime-count", type=int, default=1000)
                parser.add_argument("--base-frequency", type=float, default=220.0)
                parser.add_argument("--num-notes", type=int, default=8)
                parser.add_argument("--window-size", type=float, default=0.007)
                parser.add_argument("--density-resolution", type=int, default=4000)
                parser.add_argument("--mode", choices=["valley", "peak"], default="valley")
                parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
                parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
                parser.add_argument("--weight-curve", type=float, default=1.0)
                parser.set_defaults(include_bounds=True)
            
                args = parser.parse_args()
            
                generate_terrain_scale(
                    prime_count=args.prime_count,
                    base_frequency=args.base_frequency,
                    num_notes=args.num_notes,
                    window_size=args.window_size,
                    density_resolution=args.density_resolution,
                    mode=args.mode,
                    include_bounds=args.include_bounds,
                    weight_curve=args.weight_curve
                )
            ```

            `scripts/core_terrain_scale_final.py`
            ```py
            # ===[ IMPORTS & CONSTANTS ]===
            import argparse
            import json
            import math
            import os
            
            # ===[ PRIME UTILITIES ]===
            def generate_primes(n):
                primes = [2]
                candidate = 3
                while len(primes) < n:
                    is_prime = True
                    for p in primes:
                        if candidate % p == 0:
                            is_prime = False
                            break
                        if p * p > candidate:
                            break
                    if is_prime:
                        primes.append(candidate)
                    candidate += 2
                return primes
            
            def reduce_value(val):
                while val >= 2:
                    val /= 2
                while val < 1:
                    val *= 2
                return val
            
            # ===[ DENSITY LENS PROFILE ]===
            def gravitational_fade(d, w, n=2.5):
                relative = d / (w / 2)
                return 1 / (1 + (relative ** n))
            
            # ===[ MAIN SCALE GENERATION ENGINE ]===
            def generate_scale(prime_count, base_frequency, num_notes, window_size, density_resolution, mode):
                primes = generate_primes(prime_count)
                print(f"✔ Generated {len(primes)} primes")
            
                log_positions = [math.log2(reduce_value(p)) for p in primes]
                weights = [1 / p for p in primes]
                print("✔ Prepared log positions and reciprocal weights")
            
                x_axis = [i / density_resolution for i in range(density_resolution)]
                density_map = []
            
                for i, x in enumerate(x_axis):
                    if i % (density_resolution // 10) == 0:
                        print(f"  > Density progress: {int(i / density_resolution * 100)}%")
                    total_weight = 0
                    for log_pos, weight in zip(log_positions, weights):
                        distance = abs(log_pos - x)
                        wrapped_distance = min(distance, 1 - distance)
                        if wrapped_distance <= window_size / 2:
                            focus = gravitational_fade(wrapped_distance, window_size)
                            total_weight += weight * focus
                    density_map.append(total_weight)
                print("✔ Completed density mapping")
            
                segment_width = 1.0 / num_notes
                selected_notes = []
            
                for i in range(num_notes):
                    segment_start = i * segment_width
                    segment_end = segment_start + segment_width
                    segment_range = [(x, d) for x, d in zip(x_axis, density_map) if segment_start <= x < segment_end]
                    if segment_range:
                        if mode == "valley":
                            best_x, _ = min(segment_range, key=lambda t: t[1])
                        elif mode == "peak":
                            best_x, _ = max(segment_range, key=lambda t: t[1])
                        else:
                            raise ValueError("Invalid mode. Use 'valley' or 'peak'.")
            
                        frequency = base_frequency * (2 ** best_x)
                        midi_note = round(69 + 12 * math.log2(frequency / 440.0))
                        cents = 1200 * best_x
            
                        selected_notes.append({
                            "log_position": best_x,
                            "frequency": frequency,
                            "midi": midi_note,
                            "cents_from_base": cents,
                            "prime_sources": []
                        })
                print("✔ Selected all notes and generating output file...")
            
                # Prepare extended metadata
                metadata = {
                    "primes": primes,
                    "prime_count": len(primes),
                    "linear_prime_positions": [reduce_value(p) for p in primes],
                    "log_prime_positions": log_positions,
                    "x_axis": x_axis,
                    "density_map": density_map,
                    "algorithm_manifest": {
                        "name": "core_terrain_scale",
                        "mode": mode,
                        "window_size": window_size,
                        "lens_profile": "gravitational"
                    }
                }
            
                scale_data = {
                    "metadata": metadata,
                    "name": f"terrain_scale_{num_notes}_{mode}",
                    "base_frequency": base_frequency,
                    "notes": selected_notes
                }
            
                filename = os.path.expanduser(f"~/prime-scale-html-viewer/output/terrain_scale_{num_notes}_{mode}.json")
                with open(filename, "w") as f:
                    json.dump(scale_data, f, indent=2)
            
                print(f"✔ Scale saved to {os.path.abspath(filename)}")
            
            # ===[ COMMAND LINE ENTRY ]===
            if __name__ == "__main__":
                parser = argparse.ArgumentParser(description="Generate a musical scale from prime terrain.")
                parser.add_argument("--prime-count", type=int, default=1000)
                parser.add_argument("--base-frequency", type=float, default=220.0)
                parser.add_argument("--num-notes", type=int, default=8)
                parser.add_argument("--window-size", type=float, default=0.007)
                parser.add_argument("--density-resolution", type=int, default=4000)
                parser.add_argument("--mode", choices=["valley", "peak"], default="valley")
            
                args = parser.parse_args()
                generate_scale(
                    prime_count=args.prime_count,
                    base_frequency=args.base_frequency,
                    num_notes=args.num_notes,
                    window_size=args.window_size,
                    density_resolution=args.density_resolution,
                    mode=args.mode
                )
            ```

            `scripts/core_terrain_scale_modified.py`
            ```py
            import argparse
            import math
            from scripts.scale_utils import (
                generate_primes,
                get_log_positions,
                prime_weight,
                circular_distance,
                generate_density_axis,
                add_bounds,
                export_json
            )
            
            # Terrain-specific smoothing function
            def gravitational_fade(d, w, n=2.5):
                relative = d / (w / 2)
                return 1 / (1 + (relative ** n))
            
            # Generate density map across log2-reduced space
            def generate_density_map(log_positions, weights, resolution, window_size):
                x_axis = generate_density_axis(resolution)
                density_map = []
            
                for x in x_axis:
                    total_weight = 0
                    for log_pos, weight in zip(log_positions, weights):
                        distance = circular_distance(log_pos, x)
                        if distance <= window_size / 2:
                            focus = gravitational_fade(distance, window_size)
                            total_weight += weight * focus
                    density_map.append(total_weight)
            
                return x_axis, density_map
            
            # Segment and select notes from density map
            def select_notes_from_density(x_axis, density_map, num_notes, base_frequency, mode):
                segment_width = 1.0 / num_notes
                selected_notes = []
            
                for i in range(num_notes):
                    segment_start = i * segment_width
                    segment_end = segment_start + segment_width
                    segment_range = [(x, d) for x, d in zip(x_axis, density_map) if segment_start <= x < segment_end]
            
                    if segment_range:
                        best_x, _ = min(segment_range, key=lambda t: t[1]) if mode == "valley" else max(segment_range, key=lambda t: t[1])
                        freq = base_frequency * (2 ** best_x)
                        selected_notes.append({
                            "log_position": best_x,
                            "frequency": freq,
                            "midi": round(69 + 12 * math.log2(freq / 440.0)),
                            "cents_from_base": 1200 * best_x,
                            "prime_sources": []
                        })
            
                return selected_notes
            
            # Full generator function
            def generate_terrain_scale(prime_count, base_frequency, num_notes, window_size, density_resolution, mode, include_bounds=True, weight_curve=1.0):
                primes = generate_primes(prime_count)
                log_positions = get_log_positions(primes)
                weights = [prime_weight(p, weight_curve) for p in primes]
            
                x_axis, density_map = generate_density_map(log_positions, weights, density_resolution, window_size)
                selected_notes = select_notes_from_density(x_axis, density_map, num_notes, base_frequency, mode)
            
                if include_bounds:
                    selected_notes = add_bounds(selected_notes, base_frequency)
            
                scale_data = {
                    "name": f"terrain_scale_{num_notes}_{mode}",
                    "base_frequency": base_frequency,
                    "notes": selected_notes,
                    "log_prime_positions": log_positions,
                    "segment_boundaries": [i / num_notes for i in range(num_notes + 1)]
                }
            
                filename = f"output/terrain_scale_{num_notes}_{mode}.json"
                export_json(scale_data, filename)
            
            # CLI runner
            if __name__ == "__main__":
                parser = argparse.ArgumentParser()
                parser.add_argument("--prime-count", type=int, default=1000)
                parser.add_argument("--base-frequency", type=float, default=220.0)
                parser.add_argument("--num-notes", type=int, default=8)
                parser.add_argument("--window-size", type=float, default=0.007)
                parser.add_argument("--density-resolution", type=int, default=4000)
                parser.add_argument("--mode", choices=["valley", "peak"], default="valley")
                parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
                parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
                parser.add_argument("--weight-curve", type=float, default=1.0)
                parser.set_defaults(include_bounds=True)
            
                args = parser.parse_args()
            
                generate_terrain_scale(
                    prime_count=args.prime_count,
                    base_frequency=args.base_frequency,
                    num_notes=args.num_notes,
                    window_size=args.window_size,
                    density_resolution=args.density_resolution,
                    mode=args.mode,
                    include_bounds=args.include_bounds,
                    weight_curve=args.weight_curve
                )
            ```

            `scripts/gap_threshold_scout.py`
            ```py
            import argparse
            import math
            from scripts.scale_utils import (
                generate_primes,
                get_log_positions,
                add_bounds,
                export_json,
                generate_density_axis  # included for compatibility or plotting if needed
            )
            
            # Count qualifying gaps for a given threshold
            def detect_gap_count(log_positions, threshold):
                log_positions.sort()
                gap_centers = []
            
                for i in range(len(log_positions) - 1):
                    gap = log_positions[i + 1] - log_positions[i]
                    if gap >= threshold:
                        center_log = (log_positions[i] + log_positions[i + 1]) / 2
                        gap_centers.append(center_log)
            
                return gap_centers
            
            # Scan thresholds to find ones that match note goal
            def scan_thresholds(prime_count, threshold_min, threshold_max, step_size, note_goal, tolerance, base_frequency, include_bounds, density_resolution):
                primes = generate_primes(prime_count)
                log_positions = get_log_positions(primes)
                matches = []
            
                # Optional: could use this for visual overlays or precision matching later
                _ = generate_density_axis(density_resolution)
            
                current = threshold_min
                while current <= threshold_max:
                    gap_centers = detect_gap_count(log_positions, current)
                    count = len(gap_centers)
            
                    if abs(count - note_goal) <= tolerance:
                        print(f"✔ Match: {count} notes at threshold {current:.6f}")
                        matches.append((current, count, gap_centers))
                    else:
                        print(f"... Skipped: {count} notes at threshold {current:.6f}")
            
                    current = round(current + step_size, 10)  # Avoid float rounding errors
            
                if matches:
                    best_thresh, best_count, best_centers = matches[0]
                    notes = []
                    for log_pos in best_centers:
                        freq = base_frequency * (2 ** log_pos)
                        notes.append({
                            "log_position": log_pos,
                            "frequency": freq,
                            "midi": round(69 + 12 * math.log2(freq / 440.0)),
                            "cents_from_base": 1200 * log_pos,
                            "prime_sources": []
                        })
            
                    if include_bounds:
                        notes = add_bounds(notes, base_frequency)
            
                    scale_data = {
                        "name": f"gap_scout_match_{best_count}_notes",
                        "base_frequency": base_frequency,
                        "notes": notes
                    }
            
                    export_json(scale_data, f"gap_scout_match_{best_count}_notes.json")
                else:
                    print("No matching thresholds found within specified range.")
            
            if __name__ == "__main__":
                parser = argparse.ArgumentParser()
                parser.add_argument("--prime-count", type=int, required=True)
                parser.add_argument("--base-frequency", type=float, default=220.0)
                parser.add_argument("--threshold-range", nargs=2, type=float, required=True, metavar=("MIN", "MAX"))
                parser.add_argument("--step-size", type=float, default=0.001)
                parser.add_argument("--note-goal", type=int, required=True)
                parser.add_argument("--tolerance", type=int, default=1)
                parser.add_argument("--density-resolution", type=int, default=4000)
                parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
                parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
                parser.set_defaults(include_bounds=True)
            
                args = parser.parse_args()
            
                scan_thresholds(
                    prime_count=args.prime_count,
                    threshold_min=args.threshold_range[0],
                    threshold_max=args.threshold_range[1],
                    step_size=args.step_size,
                    note_goal=args.note_goal,
                    tolerance=args.tolerance,
                    base_frequency=args.base_frequency,
                    include_bounds=args.include_bounds,
                    density_resolution=args.density_resolution
                )
            ```

            `scripts/main.py`
            ```py
            """
            Prime Scale App – CLI Entry Point
            
            Usage (run from project root):
              python -m scripts.main --scale-type terrain ...
              python -m scripts.main --scale-type gap ...
              python -m scripts.main --scale-type pure ...
            """
            #comment hashes are used to toggle between different implementations
            import argparse
            #from scripts.core_terrain_scale import generate_terrain_scale
            from scripts.gap_threshold_scout import scan_thresholds
            from scripts.core_pure_prime_scale import generate_pure_prime_scale
            from scripts.core_terrain_scale_modified import generate_terrain_scale
            
            def main():
                parser = argparse.ArgumentParser(description="Prime Scale Generator CLI")
                subparsers = parser.add_subparsers(dest="scale_type", required=True, help="Scale type to generate")
            
                # Terrain scale CLI
                terrain_parser = subparsers.add_parser("terrain", help="Generate terrain-based scale")
                terrain_parser.add_argument("--prime-count", type=int, default=1000)
                terrain_parser.add_argument("--base-frequency", type=float, default=220.0)
                terrain_parser.add_argument("--num-notes", type=int, default=8)
                terrain_parser.add_argument("--window-size", type=float, default=0.007)
                terrain_parser.add_argument("--density-resolution", type=int, default=4000)
                terrain_parser.add_argument("--mode", choices=["valley", "peak"], default="valley")
                terrain_parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
                terrain_parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
                terrain_parser.add_argument("--weight-curve", type=float, default=1.0)
                terrain_parser.set_defaults(include_bounds=True)
            
                # Gap scale CLI
                gap_parser = subparsers.add_parser("gap", help="Generate gap-based scale")
                gap_parser.add_argument("--prime-count", type=int, required=True)
                gap_parser.add_argument("--base-frequency", type=float, default=220.0)
                gap_parser.add_argument("--threshold-range", nargs=2, type=float, required=True, metavar=("MIN", "MAX"))
                gap_parser.add_argument("--step-size", type=float, default=0.001)
                gap_parser.add_argument("--note-goal", type=int, required=True)
                gap_parser.add_argument("--tolerance", type=int, default=1)
                gap_parser.add_argument("--density-resolution", type=int, default=4000)
                gap_parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
                gap_parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
                gap_parser.set_defaults(include_bounds=True)
            
                # Pure scale CLI
                pure_parser = subparsers.add_parser("pure", help="Generate raw prime scale")
                pure_parser.add_argument("--prime-count", type=int, required=True)
                pure_parser.add_argument("--base-frequency", type=float, default=220.0)
                pure_parser.add_argument("--density-resolution", type=int, default=4000)
                pure_parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
                pure_parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
                pure_parser.set_defaults(include_bounds=True)
            
                args = parser.parse_args()
            
                if args.scale_type == "terrain":
                    generate_terrain_scale(
                        prime_count=args.prime_count,
                        base_frequency=args.base_frequency,
                        num_notes=args.num_notes,
                        window_size=args.window_size,
                        density_resolution=args.density_resolution,
                        mode=args.mode,
                        include_bounds=args.include_bounds,
                        weight_curve=args.weight_curve
                    )
            
                elif args.scale_type == "gap":
                    scan_thresholds(
                        prime_count=args.prime_count,
                        threshold_min=args.threshold_range[0],
                        threshold_max=args.threshold_range[1],
                        step_size=args.step_size,
                        note_goal=args.note_goal,
                        tolerance=args.tolerance,
                        base_frequency=args.base_frequency,
                        include_bounds=args.include_bounds,
                        density_resolution=args.density_resolution
                    )
            
                elif args.scale_type == "pure":
                    generate_pure_prime_scale(
                        prime_count=args.prime_count,
                        base_frequency=args.base_frequency,
                        include_bounds=args.include_bounds,
                        density_resolution=args.density_resolution
                    )
            
            if __name__ == "__main__":
                main()
            ```

            `scripts/scale_utils.py`
            ```py
            import math
            import json
            import os
            
            def generate_primes(n):
                primes = [2]
                candidate = 3
                while len(primes) < n:
                    is_prime = True
                    for p in primes:
                        if candidate % p == 0:
                            is_prime = False
                            break
                        if p * p > candidate:
                            break
                    if is_prime:
                        primes.append(candidate)
                    candidate += 2
                return primes
            
            def reduce_value(val):
                while val >= 2:
                    val /= 2
                while val < 1:
                    val *= 2
                return val
            
            def get_log_positions(primes):
                """Return log2 positions of primes reduced to the 1–2 octave range."""
                return [math.log2(reduce_value(p)) for p in primes]
            
            def generate_density_axis(resolution):
                """Returns evenly spaced samples from 0 to 1 (not inclusive) for log-space rendering."""
                return [i / resolution for i in range(resolution)]
            
            def circular_distance(a, b):
                return min(abs(a - b), 1 - abs(a - b))
            
            def prime_weight(p, curve=1.0):
                if curve == 0.0:
                    return 1.0
                return 1 / (p ** curve)
            
            def add_bounds(notes, base_freq):
                bounds = [
                    {
                        "log_position": 0.0,
                        "frequency": base_freq,
                        "midi": round(69 + 12 * math.log2(base_freq / 440.0)),
                        "cents_from_base": 0.0,
                        "prime_sources": []
                    },
                    {
                        "log_position": 1.0,
                        "frequency": base_freq * 2,
                        "midi": round(69 + 12 * math.log2((base_freq * 2) / 440.0)),
                        "cents_from_base": 1200.0,
                        "prime_sources": []
                    }
                ]
                return [bounds[0]] + notes + [bounds[1]]
            
            def export_json(scale_data, filename):
                # Always write to top-level /output/ folder
                script_dir = os.path.dirname(os.path.abspath(__file__))
                project_root = os.path.dirname(script_dir)
                output_dir = os.path.join(project_root, "output")
            
                os.makedirs(output_dir, exist_ok=True)
                full_path = os.path.join(output_dir, os.path.basename(filename))
            
                with open(full_path, "w", encoding="utf-8") as f:
                    json.dump(scale_data, f, indent=2)
            
                print(f"✔ Saved scale to {full_path}")
            ```

        `viewer.js`
        ```js
        const scaleDisplay = document.getElementById('scale-display');
        const canvas = document.getElementById('line-readout');
        const ctx = canvas.getContext('2d');
        
        function drawLineReadout(scale) {
          ctx.clearRect(0, 0, canvas.width, canvas.height);
        
          const primeY = canvas.height / 2;
          const noteY = primeY - 10; // Slight offset above prime ticks
        
          // Draw base prime line
          ctx.beginPath();
          ctx.moveTo(0, primeY);
          ctx.lineTo(canvas.width, primeY);
          ctx.strokeStyle = '#888';
          ctx.lineWidth = 1;
          ctx.stroke();
        
          // Draw note guide line
          ctx.beginPath();
          ctx.moveTo(0, noteY);
          ctx.lineTo(canvas.width, noteY);
          ctx.strokeStyle = '#bbb';
          ctx.lineWidth = 0.5;
          ctx.stroke();
        
          // Draw segment boundaries
          if (scale.segment_boundaries) {
            ctx.strokeStyle = '#ccc';
            scale.segment_boundaries.forEach(pos => {
              const x = pos * canvas.width;
              ctx.beginPath();
              ctx.moveTo(x, 0);
              ctx.lineTo(x, canvas.height);
              ctx.stroke();
            });
          }
        
          // Draw reduced primes
          if (scale.log_prime_positions) {
            ctx.fillStyle = '#888';
            scale.log_prime_positions.forEach(pos => {
              const x = pos * canvas.width;
              ctx.fillRect(x, primeY - 5, 1, 10);
            });
          }
        
          // Draw selected notes slightly above the prime line
          ctx.fillStyle = 'black';
          scale.notes.forEach(note => {
            const x = note.log_position * canvas.width;
            ctx.beginPath();
            ctx.arc(x, noteY, 4, 0, 2 * Math.PI);
            ctx.fill();
          });
        }
        
        function loadScale(filename) {
          fetch('output/' + filename)
            .then(res => res.json())
            .then(scale => {
              scaleDisplay.innerHTML = '';
        
              const title = document.createElement('h2');
              title.textContent = scale.name;
              scaleDisplay.appendChild(title);
        
              scale.notes.forEach(note => {
                const btn = document.createElement('button');
                btn.textContent = `${note.frequency.toFixed(2)} Hz`;
                btn.onclick = () => {
                  const ctx = new (window.AudioContext || window.webkitAudioContext)();
                  const osc = ctx.createOscillator();
                  osc.type = 'sine';
                  osc.frequency.value = note.frequency;
                  osc.connect(ctx.destination);
                  osc.start();
                  osc.stop(ctx.currentTime + 0.5);
                };
                scaleDisplay.appendChild(btn);
                scaleDisplay.appendChild(document.createTextNode(` → ${note.cents_from_base.toFixed(2)} cents`));
                scaleDisplay.appendChild(document.createElement('br'));
              });
        
              drawLineReadout(scale);
            })
            .catch(err => {
              scaleDisplay.textContent = 'Failed to load scale file.';
              console.error(err);
            });
        }
        
        // Fetch manifest.json to populate dropdown
        fetch('output/manifest.json')
          .then(res => res.json())
          .then(manifest => {
            const dropdown = document.createElement('select');
            dropdown.onchange = () => loadScale(dropdown.value);
        
            manifest.scales.forEach(file => {
              const option = document.createElement('option');
              option.value = file;
              option.textContent = file;
              dropdown.appendChild(option);
            });
        
            document.body.insertBefore(dropdown, scaleDisplay);
            if (manifest.scales.length > 0) {
              loadScale(manifest.scales[0]);
            }
          })
          .catch(err => {
            scaleDisplay.textContent = 'Failed to load manifest file.';
            console.error(err);
          });
        ```
