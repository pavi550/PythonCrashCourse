import json

input_json = """
{
  "oci_database": {
    "namespace": "oci_database",
    "metrics": {
      "CpuUtilization": {
        "alarm_query": "CpuUtilization[5m].mean() > 95",
        "alarm_severity": "CRITICAL"
      },
      "StorageUtilization": {
        "alarm_query": "StorageUtilization[5m].mean() > 95",
        "alarm_severity": "CRITICAL"
      },
      "StorageUtilizationByTablespace": {
        "alarm_query": "StorageUtilizationByTablespace[5m].mean() > 95",
        "alarm_severity": "CRITICAL"
      }
    }
  },
  "oci_database_cluster": {
    "namespace": "oci_database_cluster",
    "metrics": {
      "ASMDiskgroupUtilization": {
        "alarm_query": "ASMDiskgroupUtilization[5m].mean() > 95",
        "alarm_severity": "CRITICAL"
      },
      "CpuUtilization": {
        "alarm_query": "CpuUtilization[5m].mean() > 95",
        "alarm_severity": "CRITICAL"
      },
      "FilesystemUtilization": {
        "alarm_query": "FilesystemUtilization[5m].mean() > 95",
        "alarm_severity": "CRITICAL"
      },
      "MemoryUtilization": {
        "alarm_query": "MemoryUtilization[5m].mean() > 95",
        "alarm_severity": "CRITICAL"
      },
      "NodeStatus": {
        "alarm_query": "NodeStatus[5m].mean() < 1",
        "alarm_severity": "CRITICAL"
      }
    }
  },
  "oci_autonomous_database": {
    "namespace": "oci_autonomous_database",
    "metrics": {
      "CpuUtilization": {
        "alarm_query": "CpuUtilization[5m].mean() > 95",
        "alarm_severity": "CRITICAL"
      },
      "StorageUtilization": {
        "alarm_query": "StorageUtilization[5m].mean() > 95",
        "alarm_severity": "CRITICAL"
      },
      "DatabaseAvailability": {
        "alarm_query": "DatabaseAvailability[5m].mean() < 1",
        "alarm_severity": "CRITICAL"
      },
      "ConnectionLatency": {
        "alarm_query": "ConnectionLatency[5m].mean() > 300000",
        "alarm_severity": "CRITICAL"
      }
    }
  },
  "oci_computeagent": {
    "namespace": "oci_computeagent",
    "metrics": {
      "CpuUtilization": {
        "alarm_query": "CpuUtilization[5m].mean() > 95",
        "alarm_severity": "CRITICAL"
      },
      "MemoryUtilization": {
        "alarm_query": "MemoryUtilization[5m].mean() > 95",
        "alarm_severity": "CRITICAL"
      }
    }
  },
  "oci_compute_infrastructure_health": {
    "namespace": "oci_compute_infrastructure_health",
    "metrics": {
      "instance_status": {
        "alarm_query": "instance_status[5m].mean() > 0",
        "alarm_severity": "CRITICAL"
      },
      "maintenance_status-doubt": {
        "alarm_query": "maintenance_status[5m].mean() > 0",
        "alarm_severity": "CRITICAL"
      }
    }
  },
  "oci_fastconnect": {
    "namespace": "oci_fastconnect",
    "metrics": {
      "PacketsError": {
        "alarm_query": "PacketsError[5m].mean() > 10000000",
        "alarm_severity": "CRITICAL"
      },
      "ConnectionState": {
        "alarm_query": "ConnectionState[5m].mean() < 1",
        "alarm_severity": "CRITICAL"
      }
    }
  },
  "oci_lbaas": {
    "namespace": "oci_lbaas",
    "metrics": {
      "ActiveConnections": {
        "alarm_query": "ActiveConnections[5m].count() > 100",
        "alarm_severity": "CRITICAL"
      },
      "PeakBandwidth": {
        "alarm_query": "PeakBandwidth[5m].mean() > 800000000",
        "alarm_severity": "CRITICAL"
      }
    }
  },
  "oci_service_gateway": {
    "namespace": "oci_service_gateway",
    "metrics": {
      "sgwDropsFromService": {
        "alarm_query": "sgwDropsFromService[5m].mean() > 10",
        "alarm_severity": "CRITICAL"
      },
      "sgwDropsToService": {
        "alarm_query": "sgwDropsToService[5m].mean() > 10",
        "alarm_severity": "CRITICAL"
      }
    }
  },
  "oci_vcn": {
    "namespace": "oci_vcn",
    "metrics": {
      "VnicConntrackIsFull": {
        "alarm_query": "VnicConntrackIsFull[5m].mean() > 0",
        "alarm_severity": "CRITICAL"
      },
      "VnicEgressDropsConntrackFull": {
        "alarm_query": "VnicEgressDropsConntrackFull[5m].mean() > 0",
        "alarm_severity": "CRITICAL"
      },
      "VnicIngressDropsConntrackFull": {
        "alarm_query": "VnicIngressDropsConntrackFull[5m].mean() > 0",
        "alarm_severity": "CRITICAL"
      },
      "VnicConntrackUtilPercent": {
        "alarm_query": "VnicConntrackUtilPercent[5m].mean() > 80",
        "alarm_severity": "CRITICAL"
      }
    }
  }
}
"""

# Load the JSON input
data = json.loads(input_json)

# Function to convert JSON data to Terraform scripts
def convert_to_terraform(data):
    terraform_scripts = []
    for resource, details in data.items():
        namespace = details["namespace"]
        metrics = details["metrics"]
        
        for metric, metric_details in metrics.items():
            alarm_query = metric_details["alarm_query"]
            alarm_severity = metric_details["alarm_severity"]
            
            terraform_script = f"""
resource "oci_monitoring_alarm" "{resource}_{metric}" {{
  display_name         = "{resource}_{metric}"
  namespace            = "{namespace}"
  query                = "{alarm_query}"
  severity             = "{alarm_severity}"
  is_enabled           = true
  alarm_description    = "{metric} alarm for {resource}"
  
  destinations = [
    oci_monitoring_notification_topic.example.id
  ]

  metric_compartment_id = var.compartment_ocid
  compartment_id        = var.compartment_ocid
}}
"""
            terraform_scripts.append(terraform_script)
    
    return terraform_scripts

# Convert the JSON to Terraform scripts
terraform_scripts = convert_to_terraform(data)

# Print the generated Terraform scripts
for script in terraform_scripts:
    print(script)
