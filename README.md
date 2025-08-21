# recruitment-tasks

flowchart TD

    A[Developer] -->|git push| B[Git Repository]

    B --> C[CI Pipeline Trigger]

    subgraph CI[Continuous Integration]
        C --> D[Build & Compile]
        D --> E[Static Code Analysis / Lint]
        E --> F[Unit Tests]
        F --> G[Integration Tests]
    end

    G --> H[Artifact Repository / Docker Registry]

    subgraph CD[Continuous Delivery / Deployment]
        H --> I[Deploy to Staging]
        I --> J[Automated Tests: E2E / QA]
        J --> K{Manual Approval?}
        K -->|Yes| L[Deploy to Production]
        K -->|No| J
        L --> M[Monitoring & Alerts]
    end
