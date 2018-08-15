# Pull from Ubuntu 16.04 image
Bootstrap: debootstrap
OSVersion: xenial
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

# Copy over files
%files
    main.py /
    requirements.txt /

%post
    # Create a directory to hold our scripts
    mkdir /app
    mv /main.py /app/
    mv /requirements.txt /app/

    # Make logs and results directories
    mkdir /logs
    mkdir /results

    # Install Python 3.5 and Pip
    apt-get install -y software-properties-common
    apt-add-repository universe
    apt-get update
    apt-get install -y python3-pip

    # Install Python requirements
    pip3 install -r /app/requirements.txt
