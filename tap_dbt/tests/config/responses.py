import json

ACCOUNT = '''{
    "status": {
        "code": 200,
        "is_success": true,
        "user_message": "Success!",
        "developer_message": ""
    },
    "data": {
        "docs_job_id": null,
        "freshness_job_id": null,
        "lock_reason": null,
        "unlock_if_subscription_renewed": false,
        "read_only_seats": 3,
        "id": 1001,
        "name": "Corp",
        "state": 42,
        "plan": "enterprise",
        "pending_cancel": false,
        "run_slots": 3,
        "developer_seats": 3,
        "queue_limit": 50,
        "pod_memory_request_mebibytes": 600,
        "run_duration_limit_seconds": 900,
        "enterprise_authentication_method": null,
        "enterprise_login_slug": null,
        "enterprise_unique_identifier": null,
        "billing_email_address": null,
        "locked": false,
        "develop_file_system": true,
        "unlocked_at": null,
        "created_at": "2022-01-01T00:42:00.000000+00:00",
        "updated_at": "2022-01-31T23:59:42.000000+00:00",
        "starter_repo_url": null,
        "sso_reauth": false,
        "force_sso": true,
        "git_auth_level": "personal",
        "identifier": "act_xyzwq",
        "docs_job": null,
        "freshness_job": null,
        "enterprise_login_url": "https://cloud.corp.getdbt.com/enterprise-login/None/"
    }
}'''


JOBS = '''
{
    "status": {
        "code": 200,
        "is_success": true,
        "user_message": "Success!",
        "developer_message": ""
    },
    "data": [
        {
            "execution": {
                "timeout_seconds": 0
            },
            "generate_docs": true,
            "run_generate_sources": false,
            "id": 1,
            "account_id": 1001,
            "project_id": 1,
            "environment_id": 1,
            "name": "Yay dbt Job!",
            "dbt_version": null,
            "created_at": "2022-08-15T15:15:15.000000+00:00",
            "updated_at": "2022-08-15T15:15:16.000001+00:00",
            "execute_steps": [
                "dbt build"
            ],
            "state": 1,
            "deactivated": false,
            "run_failure_count": 0,
            "deferring_job_definition_id": null,
            "lifecycle_webhooks": false,
            "lifecycle_webhooks_url": null,
            "triggers": {
                "github_webhook": false,
                "git_provider_webhook": false,
                "custom_branch_only": false,
                "schedule": false
            },
            "settings": {
                "threads": 4,
                "target_name": "default"
            },
            "schedule": {
                "cron": "0 * * * *",
                "date": {
                    "type": "every_day"
                },
                "time": {
                    "type": "every_hour",
                    "interval": 1
                }
            },
            "is_deferrable": false,
            "generate_sources": false,
            "cron_humanized": "Every hour",
            "next_run": null,
            "next_run_humanized": null
        },
        {
            "execution": {
                "timeout_seconds": 0
            },
            "generate_docs": false,
            "run_generate_sources": false,
            "id": 2,
            "account_id": 1001,
            "project_id": 1,
            "environment_id": 1,
            "name": "My second dbt Job",
            "dbt_version": null,
            "created_at": "2022-07-31T11:01:30.000000+00:00",
            "updated_at": "2022-08-31T12:01:30.000000+00:00",
            "execute_steps": [
                "dbt run"
            ],
            "state": 1,
            "deactivated": false,
            "run_failure_count": 0,
            "deferring_job_definition_id": null,
            "lifecycle_webhooks": false,
            "lifecycle_webhooks_url": null,
            "triggers": {
                "github_webhook": true,
                "git_provider_webhook": false,
                "custom_branch_only": false,
                "schedule": false
            },
            "settings": {
                "threads": 4,
                "target_name": "default"
            },
            "schedule": {
                "cron": "0 * * * *",
                "date": {
                    "type": "every_day"
                },
                "time": {
                    "type": "every_hour",
                    "interval": 1
                }
            },
            "is_deferrable": false,
            "generate_sources": false,
            "cron_humanized": "Every hour",
            "next_run": null,
            "next_run_humanized": null
        }
    ],
    "extra": {
        "filters": {
            "limit": 100,
            "offset": 0,
            "account_id": 1001
        },
        "order_by": "id",
        "pagination": {
            "count": 1,
            "total_count": 2
        }
    }
}
'''


PROJECTS = '''
{
    "status": {
        "code": 200,
        "is_success": true,
        "user_message": "Success!",
        "developer_message": ""
    },
    "data": [
        {
            "name": "Sales dbt Project",
            "account_id": 1001,
            "repository_id": 29,
            "connection_id": 1,
            "id": 1,
            "created_at": "2021-11-02 08:33:57.867705+00:00",
            "updated_at": "2021-12-28 11:26:30.042923+00:00",
            "skipped_setup": false,
            "state": 1,
            "dbt_project_subdirectory": null,
            "connection": {
                "id": 1,
                "account_id": 1001,
                "project_id": 1,
                "name": "DEV Snowflake",
                "type": "snowflake",
                "created_by_id": 3,
                "created_by_service_token_id": null,
                "details": {
                    "account": "xy12345.us-north.azure",
                    "database": "dwh",
                    "warehouse": "compute_wh",
                    "allow_sso": true,
                    "client_session_keep_alive": false,
                    "role": "dwh_system"
                },
                "state": 1,
                "created_at": "2021-11-10 09:09:00.000005+00:00",
                "updated_at": "2021-11-10 09:09:00.000005+00:00"
            },
            "repository": {
                "id": 29,
                "account_id": 1001,
                "project_id": 1,
                "full_name": "corp/sales-dbt-project",
                "remote_url": "git://github.com/corp/sales-dbt-project.git",
                "remote_backend": "github",
                "git_clone_strategy": "github_app",
                "deploy_key_id": 29,
                "repository_credentials_id": null,
                "github_installation_id": 21729016,
                "pull_request_url_template": "https://github.com/corp/sales-dbt-project/compare/{{destination}}...{{source}}",
                "state": 1,
                "created_at": "2021-11-10 09:09:00.000005+00:00",
                "updated_at": "2021-11-10 09:09:59.000006+00:00",
                "deploy_key": {
                    "id": 3,
                    "account_id": 1001,
                    "state": 1,
                    "public_key": "ssh-rsa abc...xyz"
                },
                "github_repo": "corp/sales-dbt-project",
                "name": "sales-dbt-project",
                "git_provider_id": 2,
                "gitlab": null,
                "git_provider": null
            },
            "group_permissions": [
                {
                    "account_id": 1001,
                    "group_id": 3,
                    "project_id": 2,
                    "all_projects": false,
                    "permission_set": "readonly",
                    "permission_level": null,
                    "id": 3,
                    "state": 1,
                    "created_at": "2021-11-12 09:19:01.000006+00:00",
                    "updated_at": "2021-11-13 09:19:59.000006+00:00"
                }
            ],
            "docs_job_id": null,
            "freshness_job_id": null,
            "docs_job": null,
            "freshness_job": null
        },
        {
            "name": "Sales Project",
            "account_id": 1001,
            "repository_id": 3,
            "connection_id": 1,
            "id": 2,
            "created_at": "2021-11-15 10:09:59.000006+00:00",
            "updated_at": "2021-11-16 11:59:59.000006+00:00",
            "skipped_setup": false,
            "state": 1,
            "dbt_project_subdirectory": null,
            "connection": {
                "id": 2,
                "account_id": 1001,
                "project_id": 2,
                "name": "Cloud DWH",
                "type": "snowflake",
                "created_by_id": 2,
                "created_by_service_token_id": null,
                "details": {
                    "account": "xy12345.snowflakecomputing.com",
                    "database": "dwh",
                    "warehouse": "compute_wh",
                    "allow_sso": true,
                    "client_session_keep_alive": true,
                    "role": "dwh_system"
                },
                "state": 1,
                "created_at": "2021-10-12 13:12:12.000020+00:00",
                "updated_at": "2021-10-12 13:12:13.000030+00:00"
            },
            "repository": {
                "id": 2,
                "account_id": 1001,
                "project_id": 1,
                "full_name": null,
                "remote_url": "gh repo clone my-corp/dbt-data-project",
                "remote_backend": null,
                "git_clone_strategy": "deploy_key",
                "deploy_key_id": 3,
                "repository_credentials_id": null,
                "github_installation_id": null,
                "pull_request_url_template": null,
                "state": 1,
                "created_at": "2021-10-12 12:12:12.000020+00:00",
                "updated_at": "2021-10-12 12:12:12.000021+00:00",
                "deploy_key": {
                    "id": 1,
                    "account_id": 1001,
                    "state": 1,
                    "public_key": "ssh-rsa abc...xyz"
                },
                "github_repo": null,
                "name": null,
                "git_provider_id": 1,
                "gitlab": null,
                "git_provider": null
            },
            "group_permissions": [],
            "docs_job_id": null,
            "freshness_job_id": null,
            "docs_job": null,
            "freshness_job": null
        }
    ],
    "extra": {
        "filters": {
            "account_id": 1001,
            "limit": 2,
            "offset": 0
        },
        "order_by": "id",
        "pagination": {
            "count": 2,
            "total_count": 2
        }
    }
}
'''


RUNS = '''
{
    "status": {
        "code": 200,
        "is_success": true,
        "user_message": "Success!",
        "developer_message": ""
    },
    "data": [
        {
            "id": 1,
            "trigger_id": 1,
            "account_id": 1001,
            "environment_id": 1,
            "project_id": 1,
            "job_definition_id": 1,
            "status": 20,
            "dbt_version": "1.21.0",
            "git_branch": "dev",
            "git_sha": "abcasddfg123345",
            "status_message": null,
            "owner_thread_id": null,
            "executed_by_thread_id": "dbt-run-1-wx0xw",
            "deferring_run_id": null,
            "artifacts_saved": true,
            "artifact_s3_path": "bucket/runs/1/artifacts/target",
            "has_docs_generated": true,
            "has_sources_generated": false,
            "notifications_sent": true,
            "blocked_by": [],
            "scribe_enabled": false,
            "created_at": "2021-11-11 11:11:11.111115+00:00",
            "updated_at": "2021-11-11 11:11:21.111115+00:00",
            "dequeued_at": "2021-11-11 11:11:31.111115+00:00",
            "started_at": "2021-11-11 11:11:51.111115+00:00",
            "finished_at": "2021-11-11 11:12:11.111115+00:00",
            "last_checked_at": null,
            "last_heartbeat_at": null,
            "should_start_at": null,
            "trigger": null,
            "job": null,
            "environment": null,
            "run_steps": [],
            "status_humanized": "Error",
            "in_progress": false,
            "is_complete": true,
            "is_success": false,
            "is_error": true,
            "is_cancelled": false,
            "href": "https://cloud.corp.getdbt.com/next/deploy/1001/projects/1/runs/2/",
            "duration": "00:00:30",
            "queued_duration": "00:00:15",
            "run_duration": "00:00:15",
            "duration_humanized": "30 seconds",
            "queued_duration_humanized": "15 seconds",
            "run_duration_humanized": "15 seconds",
            "created_at_humanized": "1 month ago",
            "finished_at_humanized": "1 month ago",
            "job_id": 1,
            "is_running": null
        },
        {
            "id": 1,
            "trigger_id": 1,
            "account_id": 1001,
            "environment_id": 1,
            "project_id": 1,
            "job_definition_id": 1,
            "status": 20,
            "dbt_version": "1.0.1",
            "git_branch": "main",
            "git_sha": "98765asdfgh",
            "status_message": null,
            "owner_thread_id": null,
            "executed_by_thread_id": "dbt-run-1-xyzwq",
            "deferring_run_id": null,
            "artifacts_saved": true,
            "artifact_s3_path": "bucket/runs/1/artifacts/target",
            "has_docs_generated": true,
            "has_sources_generated": false,
            "notifications_sent": true,
            "blocked_by": [],
            "scribe_enabled": false,
            "created_at": "2021-11-11 11:11:11.111115+00:00",
            "updated_at": "2021-11-12 11:11:11.111114+00:00",
            "dequeued_at": "2021-11-13 11:11:11.111113+00:00",
            "started_at": "2021-11-14 11:11:11.111112+00:00",
            "finished_at": "2021-11-15 11:11:11.111111+00:00",
            "last_checked_at": null,
            "last_heartbeat_at": null,
            "should_start_at": "2021-11-15 15:28:21.481369+00:00",
            "trigger": null,
            "job": null,
            "environment": null,
            "run_steps": [],
            "status_humanized": "Error",
            "in_progress": false,
            "is_complete": true,
            "is_success": false,
            "is_error": true,
            "is_cancelled": false,
            "href": "https://cloud.corp.getdbt.com/next/deploy/1001/projects/1/runs/1/",
            "duration": "00:00:10",
            "queued_duration": "00:00:10",
            "run_duration": "00:00:10",
            "duration_humanized": "10 seconds",
            "queued_duration_humanized": "10 seconds",
            "run_duration_humanized": "10 seconds",
            "created_at_humanized": "1 day ago",
            "finished_at_humanized": "1 day ago",
            "job_id": 1,
            "is_running": null
        }
    ],
    "extra": {
        "filters": {
            "account_id": 1001,
            "limit": 2,
            "offset": 0
        },
        "order_by": "id",
        "pagination": {
            "count": 2,
            "total_count": 5
        }
    }
}
'''