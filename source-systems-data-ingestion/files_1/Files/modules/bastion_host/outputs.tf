output "project" {
  value = var.project
}

### START CODE HERE ### (~ 19 lines of code)

# Define an output for the id of the EC2
# instance
output "bastion_host_id" {
  value = aws_instance.bastion_host.id
}

# Define an output for the public DNS of the EC2
# instance
output "bastion_host_dns" {
  value = aws_instance.bastion_host.public_dns
}

# Define an output for the hostname or address of the RDS
output "db_host" {
  value = aws_db_instance.database.address
}

# Define an output for the port of the RDS
output "db_port" {
  value = aws_db_instance.database.port
}

# Define an output for the username of the RDS
output "db_master_username" {
  value = var.db_master_username
}

# Define an output for the master password of the RDS
output "db_master_password" {
  value     = random_id.master_password.hex
  sensitive = true
}

### END CODE HERE ###