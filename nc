nc localhost 4446 << EOF
info status
info version
info kvm
info migrate_capabilities
EOF
echo
