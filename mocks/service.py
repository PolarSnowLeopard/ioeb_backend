API_IDS = {
    "predict": "1bfa846d-6fbd-4c1f-a3c9-0b476b03004e",
    "healthCheck": "cb75d13a-f01c-480d-b712-31100f943de4",
    "train": "bc069861-ab8c-4ecd-879a-5edf16fb8d0c",
    "getReportData": "12a38525-ac78-4cd4-b774-42f4d494856b",
    "sendReport": "f954d5f7-6b14-4435-a670-1df8ed84b5b4",
    "generateReport": "ef722cf8-7cf6-49e5-9933-c2df97de5336",
    "preprocess": "241ea618-ca42-42d3-849d-01feea694b0e",
    "evaluate": "25baef13-cb6f-479a-a93b-631ba7bbede9",
    "visualize": "0fc3e43d-100a-49ac-b235-78051bcd1164",
    "generate-report": "4ba7146b-2bdc-4b78-bc50-35026f466b8a",
    "nl2gql": "6b12525f-90fc-4cda-baf7-11c37d1b1618",
    "safety-fingerprint": "00c6af38-3aa2-4050-be0c-00c837c8cd42",
    "技术评测元应用": "92d23e76-b104-4924-8b15-c6588c063255",
    "无人机智能投递": "94395fbc-7349-4a06-80db-04c417f4bd04",
    "calculate": "402cb58e-5214-4a5d-b945-16f7c8651307",
    "diagnose": "53c9fa26-03db-4a99-b91f-564c49ed1651",
    "analyze": "8b00114e-2171-439a-968b-24302b2c036c",
    "alert": "d6e2cc85-ac02-4a79-98c8-b1a3155c14be",
    "transcribe": "15a001b4-cfa0-4f4e-881a-8374d650f7d7",
    "allocate": "a6c63357-3920-48aa-b0bb-6bff0887270b",
    "乡村医疗AI辅助诊断元应用": "7ead28c2-508f-45d6-9f3f-c74bf76240f3",
    "农村公共卫生监测元应用": "64177ab7-ed48-4e86-913f-f14c6d1fa397",
    "analyzeImage": "b278a7e5-d0f6-400f-a565-99f4d68cd1b2",
    "identifyDisease": "df6ee593-4d89-4685-8803-b20dd9a196cf",
    "getIrrigationPlan": "a3d0e878-abc9-4fc6-969a-c878abbf9116",
    "predictYield": "1bffe8a9-fe3d-4878-847d-9c61f72bad41",
    "智慧农业综合管理元应用": "2c54e7c3-a640-456b-a419-1a6c0c33784f",
    "pathPlanner": "43b7bde3-167b-46b6-96cb-24fc889b1130",
    "environmentPerception": "f14c260d-01f0-4869-8fbd-115f2cf2573c",
    "obstacleDetection": "ee524351-3cee-4f2e-929e-7929599f6388",
    "flightController": "c2fe7095-7724-485b-8787-cfe466151280",
    "batteryManager": "739c6576-9548-4786-9b1f-ab40b9b77951",
    "energyOptimizer": "89f279f7-7784-4b1a-addb-e2f797ac8c65",
    "safetyMonitor": "efc07658-7261-4ede-80ee-381788467468",
    "eVTOL智能飞行控制元应用": "f9b14d94-1b6e-4aca-9ec7-8fb27ffa054b",
    "translateContent": "5f5a8758-f2f2-4efa-a54b-585177f3a3b6",
    "generateDescription": "1ca5b3fc-4063-4bbf-ad3a-07e1a667b2b8",
    "analyzeTrend": "7f8dcbe8-1ffd-4553-92ef-abd030b55b86",
    "predictSales": "eca2ba57-95d6-4c94-af9c-c156f40882ee",
    "跨境电商智能营销元应用": "bfe2c424-8df7-42bf-9cfd-e4b751a116d5",
    "objectDetection": "01a6a1bf-4a6d-4bfd-85c1-e00dde8ddc80",
    "spatialMapping": "33252104-2887-463d-9fc9-aaa10ff5982d",
    "naturalLanguageUnderstanding": "de632961-6f54-4f1b-91a1-0e33990b9930",
    "emotionRecognition": "c7e7459e-25fc-4bff-96fb-0f450d467c80",
    "vitalSignsMonitor": "5e3baa59-f572-4dde-9a84-0d31208a571e",
    "abnormalBehaviorDetection": "4320d33d-5da0-4ec5-a08f-63e94c9e6ec2",
    "taskPlanner": "a4f448ad-bfe4-4bd0-957d-84784393a854",
    "pathPlanning": "b620d01c-daf1-4840-ba69-f2505147b017",
    "家庭智能助手元应用": "e4141f97-f036-484d-95e5-f58738d76011",
}

# MOCK_SERVICES 数据
MOCK_SERVICES = [
    {
        "id": "3b3d4e4d-36e4-4436-bea1-63af2117d0bc",
        "name": "课题一风险识别模型推理微服务",
        "attribute": "open_source",
        "type": "atomic",
        "domain": "aml",
        "industry": "0",
        "scenario": "1",
        "technology": "1",
        "network": "bridge",
        "port": "0.0.0.0:8000/TCP → 0.0.0.0:80000",
        "volume": "/var/opt/gitlab/mnt/user  →  /appdata/aml/data",
        "status": "released",
        "number": 512,
        "deleted": 0,
        "create_time": 1744635999632,
        "creator_id": ""
    },
    {
        "id": "4fda9469-dcd7-4032-affb-9c9df0cd2cc6",
        "name": "课题二多方安全计算模型推理微服务",
        "attribute": "open_source",
        "type": "atomic",
        "domain": "aml",
        "industry": "0",
        "scenario": "1",
        "technology": "1",
        "network": "bridge",
        "port": "0.0.0.0:8000/TCP → 0.0.0.0:80000",
        "volume": "/var/opt/gitlab/mnt/user  →  /appdata/aml/data",
        "status": "released",
        "number": 512,
        "deleted": 0,
        "create_time": 1744635999632,
        "creator_id": ""
    },
    {
        "id": "dce40ba0-b5bb-4508-bd09-38a95a2e2932",
        "name": "技术评测微服务",
        "attribute": "open_source",
        "type": "atomic",
        "domain": "aml",
        "industry": "1",
        "scenario": "2",
        "technology": "2",
        "network": "bridge",
        "port": "0.0.0.0:8001/TCP → 0.0.0.0:80001",
        "volume": "/var/opt/gitlab/mnt/user  →  /appdata/aml/data",
        "status": "error",
        "number": 8192,
        "deleted": 0,
        "create_time": 1744635999632,
        "creator_id": ""
    },
    {
        "id": "01a951d1-09b1-4d65-9f6c-cf048e5f620e",
        "name": "样例报告生成微服务",
        "attribute": "non_intelligent",
        "type": "atomic",
        "domain": "aml",
        "industry": "2",
        "scenario": "3",
        "technology": "3",
        "network": "bridge",
        "port": "0.0.0.0:8002/TCP → 0.0.0.0:80002",
        "volume": "/var/opt/gitlab/mnt/user  →  /appdata/aml/data",
        "status": "pre_release_unrated",
        "number": 2330,
        "deleted": 0,
        "create_time": 1744635999632,
        "creator_id": ""
    },
    {
        "id": "fde67dc7-39a2-4378-a5fe-ceec617d802f",
        "name": "信用评估微服务",
        "attribute": "paid",
        "type": "atomic",
        "domain": "aml",
        "industry": "3",
        "scenario": "4",
        "technology": "4",
        "network": "bridge",
        "port": "0.0.0.0:8003/TCP → 0.0.0.0:80003",
        "volume": "/var/opt/gitlab/mnt/user  →  /appdata/aml/data",
        "status": "not_deployed",
        "number": 2342,
        "deleted": 0,
        "create_time": 1744635999632,
        "creator_id": ""
    },
    {
        "id": "1f464c6b-6b49-4fa2-8ec9-6942815f7d8f",
        "name": "异常识别微服务",
        "attribute": "open_source",
        "type": "atomic",
        "domain": "aml",
        "industry": "0",
        "scenario": "0",
        "technology": "0",
        "network": "bridge",
        "port": "0.0.0.0:8004/TCP → 0.0.0.0:80004",
        "volume": "/var/opt/gitlab/mnt/user  →  /appdata/aml/data",
        "status": "error",
        "number": 0,
        "deleted": 0,
        "create_time": 1744635999632,
        "creator_id": ""
    },
    {
        "id": "b352ae47-92db-4281-8faf-9491ab6baea3",
        "name": "课题三金融风险报告生成微服务",
        "attribute": "paid",
        "type": "atomic",
        "domain": "aml",
        "industry": "3",
        "scenario": "4",
        "technology": "4",
        "network": "bridge",
        "port": "0.0.0.0:8005/TCP → 0.0.0.0:80005",
        "volume": "/var/opt/gitlab/mnt/user  →  /appdata/aml/data",
        "status": "released",
        "number": 2342,
        "deleted": 0,
        "create_time": 1744635999632,
        "creator_id": ""
    },
    {
        "id": "c482ad98-4a7b-4498-a4d5-a52f991d1c0d",
        "name": "课题四模型评测-安全性指纹微服务",
        "attribute": "paid",
        "type": "atomic",
        "domain": "aml",
        "industry": "3",
        "scenario": "4",
        "technology": "4",
        "network": "bridge",
        "port": "0.0.0.0:8006/TCP → 0.0.0.0:80006",
        "volume": "/var/opt/gitlab/mnt/user  →  /appdata/aml/data",
        "status": "released",
        "number": 2342,
        "deleted": 0,
        "create_time": 1744635999632,
        "creator_id": ""
    },
    {
        "id": "b1b8417a-145c-43e3-b0d1-1aa3d7279c6b",
        "name": "技术评测元应用",
        "attribute": "custom",
        "type": "meta",
        "domain": "aml",
        "industry": "1",
        "scenario": "2",
        "technology": "4",
        "network": "bridge",
        "port": "0.0.0.0:1020/TCP → 0.0.0.0:10020",
        "volume": "/var/opt/gitlab/mnt/user  →  /appdata/aml/metaApp",
        "status": "pre_release_pending",
        "number": 2342,
        "deleted": 0,
        "create_time": 1744635999632,
        "creator_id": ""
    },
    {
        "id": "3c93a110-4618-4b12-83fd-4b5a6f89a105",
        "name": "无人机虚拟仿真微服务",
        "attribute": "open_source",
        "type": "atomic",
        "domain": "aircraft",
        "industry": "0",
        "scenario": "0",
        "technology": "1",
        "network": "bridge",
        "port": "0.0.0.0:8080/TCP → 0.0.0.0:80080",
        "volume": "/var/opt/gitlab/mnt/user  →  /appdata/aircraft/data",
        "status": "deploying",
        "number": 2342,
        "deleted": 0,
        "create_time": 1744635999635,
        "creator_id": ""
    },
    {
        "id": "77064ca6-3a5d-49cd-8a27-c6a7b52fc20e",
        "name": "无人机低空测绘微服务",
        "attribute": "open_source",
        "type": "atomic",
        "domain": "aircraft",
        "industry": "1",
        "scenario": "3",
        "technology": "2",
        "network": "bridge",
        "port": "0.0.0.0:8081/TCP → 0.0.0.0:80081",
        "volume": "/var/opt/gitlab/mnt/user  →  /appdata/aircraft/data",
        "status": "error",
        "number": 2342,
        "deleted": 0,
        "create_time": 1744635999635,
        "creator_id": ""
    },
    {
        "id": "74e5ff68-23a9-4109-967d-a5a76f29ba6a",
        "name": "无人机目标识别微服务",
        "attribute": "open_source",
        "type": "atomic",
        "domain": "aircraft",
        "industry": "2",
        "scenario": "4",
        "technology": "2",
        "network": "bridge",
        "port": "0.0.0.0:8082/TCP → 0.0.0.0:80082",
        "volume": "/var/opt/gitlab/mnt/user  →  /appdata/aircraft/data",
        "status": "error",
        "number": 2342,
        "deleted": 0,
        "create_time": 1744635999635,
        "creator_id": ""
    },
    {
        "id": "da43a293-fb67-4efb-b65b-ec22d9cca5ae",
        "name": "无人机远程控制微服务",
        "attribute": "non_intelligent",
        "type": "atomic",
        "domain": "aircraft",
        "industry": "0",
        "scenario": "1",
        "technology": "3",
        "network": "bridge",
        "port": "0.0.0.0:8083/TCP → 0.0.0.0:80083",
        "volume": "/var/opt/gitlab/mnt/user  →  /appdata/aircraft/data",
        "status": "not_deployed",
        "number": 2342,
        "deleted": 0,
        "create_time": 1744635999635,
        "creator_id": ""
    },
    {
        "id": "aacc5100-a017-49d9-a784-c7fe210d234c",
        "name": "无人机视频分析微服务",
        "attribute": "paid",
        "type": "atomic",
        "domain": "aircraft",
        "industry": "1",
        "scenario": "2",
        "technology": "4",
        "network": "bridge",
        "port": "0.0.0.0:8084/TCP → 0.0.0.0:80084",
        "volume": "/var/opt/gitlab/mnt/user  →  /appdata/aircraft/data",
        "status": "pre_release_unrated",
        "number": 2342,
        "deleted": 0,
        "create_time": 1744635999635,
        "creator_id": ""
    },
    {
        "id": "57b897b2-f191-4ede-98d6-46aaee8bd4e8",
        "name": "无人机智能投递",
        "attribute": "custom",
        "type": "meta",
        "domain": "aircraft",
        "industry": "1",
        "scenario": "2",
        "technology": "4",
        "network": "bridge",
        "port": "0.0.0.0:8084/TCP → 0.0.0.0:80084",
        "volume": "/var/opt/gitlab/mnt/user  →  /appdata/aircraft/data",
        "status": "pre_release_unrated",
        "number": 2342,
        "deleted": 0,
        "create_time": 1744635999635,
        "creator_id": ""
    },
    {
        "id": "fa3fafbb-fb30-492d-93cf-b608e06b4d99",
        "name": "肝移植患者利奈唑胺给药方案优化微服务",
        "attribute": "open_source",
        "type": "atomic",
        "domain": "health",
        "industry": "0",
        "scenario": "1",
        "technology": "1",
        "network": "bridge",
        "port": "0.0.0.0:8000/TCP → 0.0.0.0:80000",
        "volume": "/var/opt/gitlab/mnt/user  →  /appdata/aml/data",
        "status": "released",
        "number": 512,
        "deleted": 0,
        "create_time": 1744635999641,
        "creator_id": ""
    },
    {
        "id": "f6c3c542-59ed-4277-b771-21f5191d8c5c",
        "name": "基层医疗影像辅助诊断微服务",
        "attribute": "open_source",
        "type": "atomic",
        "domain": "health",
        "industry": "0",
        "scenario": "1",
        "technology": "0",
        "network": "bridge",
        "port": "0.0.0.0:8100/TCP → 0.0.0.0:81000",
        "volume": "/var/opt/gitlab/mnt/user  →  /appdata/health/data",
        "status": "released",
        "number": 256,
        "deleted": 0,
        "create_time": 1744635999641,
        "creator_id": ""
    },
    {
        "id": "fd918206-0564-408b-a096-efd3b64c4efc",
        "name": "慢性病管理监测微服务",
        "attribute": "open_source",
        "type": "atomic",
        "domain": "health",
        "industry": "0",
        "scenario": "2",
        "technology": "2",
        "network": "bridge",
        "port": "0.0.0.0:8101/TCP → 0.0.0.0:81001",
        "volume": "/var/opt/gitlab/mnt/user  →  /appdata/health/data",
        "status": "released",
        "number": 128,
        "deleted": 0,
        "create_time": 1744635999641,
        "creator_id": ""
    },
    {
        "id": "e54ba826-ad95-45aa-928a-cea6d2d94e2a",
        "name": "方言语音识别转写微服务",
        "attribute": "paid",
        "type": "atomic",
        "domain": "aircraft",
        "industry": "0",
        "scenario": "0",
        "technology": "1",
        "network": "bridge",
        "port": "0.0.0.0:8102/TCP → 0.0.0.0:81002",
        "volume": "/var/opt/gitlab/mnt/user  →  /appdata/health/data",
        "status": "released",
        "number": 384,
        "deleted": 0,
        "create_time": 1744635999641,
        "creator_id": ""
    },
    {
        "id": "957f8b36-d0c7-462a-9041-cfb2e063f328",
        "name": "乡村医疗资源调度微服务",
        "attribute": "non_intelligent",
        "type": "atomic",
        "domain": "health",
        "industry": "1",
        "scenario": "3",
        "technology": "3",
        "network": "bridge",
        "port": "0.0.0.0:8103/TCP → 0.0.0.0:81003",
        "volume": "/var/opt/gitlab/mnt/user  →  /appdata/health/data",
        "status": "error",
        "number": 192,
        "deleted": 0,
        "create_time": 1744635999641,
        "creator_id": ""
    },
    {
        "id": "cd670e2a-8567-437d-8dd2-27eee559be19",
        "name": "流行病预测分析微服务",
        "attribute": "paid",
        "type": "atomic",
        "domain": "agriculture",
        "industry": "1",
        "scenario": "4",
        "technology": "2",
        "network": "bridge",
        "port": "0.0.0.0:8104/TCP → 0.0.0.0:81004",
        "volume": "/var/opt/gitlab/mnt/user  →  /appdata/health/data",
        "status": "released",
        "number": 512,
        "deleted": 0,
        "create_time": 1744635999641,
        "creator_id": ""
    },
    {
        "id": "fa4c11e8-e76a-49c5-903a-9634dc3abe67",
        "name": "乡村医疗AI辅助诊断元应用",
        "attribute": "custom",
        "type": "meta",
        "domain": "health",
        "industry": "0",
        "scenario": "1",
        "technology": "0",
        "network": "bridge",
        "port": "0.0.0.0:8120/TCP → 0.0.0.0:81020",
        "volume": "/var/opt/gitlab/mnt/user  →  /appdata/health/metaApp",
        "status": "pre_release_unrated",
        "number": 1024,
        "deleted": 0,
        "create_time": 1744635999641,
        "creator_id": ""
    },
    {
        "id": "80b3b5e1-f2bc-4cd2-a196-0298aa8cc57a",
        "name": "农村公共卫生监测元应用",
        "attribute": "custom",
        "type": "meta",
        "domain": "health",
        "industry": "1",
        "scenario": "4",
        "technology": "2",
        "network": "bridge",
        "port": "0.0.0.0:8121/TCP → 0.0.0.0:81021",
        "volume": "/var/opt/gitlab/mnt/user  →  /appdata/health/metaApp",
        "status": "pre_release_unrated",
        "number": 768,
        "deleted": 0,
        "create_time": 1744635999641,
        "creator_id": ""
    },
    {
        "id": "4f35b674-4a5b-4b69-a55c-ef0a0ccf2553",
        "name": "农作物图像分析服务",
        "attribute": "open_source",
        "type": "atomic",
        "domain": "agriculture",
        "industry": "4",
        "scenario": "0",
        "technology": "计算机视觉（智慧种植/精准播种）",
        "network": "bridge",
        "port": "0.0.0.0:8010/TCP → 0.0.0.0:8010",
        "volume": "/var/opt/gitlab/mnt/user → /appdata/agriculture/data",
        "status": "released",
        "number": 512,
        "deleted": 0,
        "create_time": 1744635999646,
        "creator_id": ""
    },
    {
        "id": "f6be78dc-ac2b-485f-93ec-0f7215797d21",
        "name": "病虫害识别与防治服务",
        "attribute": "open_source",
        "type": "atomic",
        "domain": "agriculture",
        "industry": "4",
        "scenario": "1",
        "technology": "计算机视觉（智慧种植/病虫害防治）",
        "network": "bridge",
        "port": "0.0.0.0:8011/TCP → 0.0.0.0:8011",
        "volume": "/var/opt/gitlab/mnt/user → /appdata/agriculture/data",
        "status": "released",
        "number": 512,
        "deleted": 0,
        "create_time": 1744635999646,
        "creator_id": ""
    },
    {
        "id": "c5f36a0f-888f-4900-b970-890b13bc0e86",
        "name": "智能灌溉决策服务",
        "attribute": "open_source",
        "type": "atomic",
        "domain": "agriculture",
        "industry": "4",
        "scenario": "2",
        "technology": "时序分析与预测（智慧种植/智能灌溉）",
        "network": "bridge",
        "port": "0.0.0.0:8012/TCP → 0.0.0.0:8012",
        "volume": "/var/opt/gitlab/mnt/user → /appdata/agriculture/data",
        "status": "released",
        "number": 512,
        "deleted": 0,
        "create_time": 1744635999646,
        "creator_id": ""
    },
    {
        "id": "241009ad-8465-44a8-befb-bfb9c000c2cb",
        "name": "农作物产量预测服务",
        "attribute": "open_source",
        "type": "atomic",
        "domain": "agriculture",
        "industry": "4",
        "scenario": "3",
        "technology": "时序分析与预测（智慧种植/产量预测）",
        "network": "bridge",
        "port": "0.0.0.0:8013/TCP → 0.0.0.0:8013",
        "volume": "/var/opt/gitlab/mnt/user → /appdata/agriculture/data",
        "status": "released",
        "number": 512,
        "deleted": 0,
        "create_time": 1744635999646,
        "creator_id": ""
    },
    {
        "id": "9fe9c51a-aa30-44b0-95ff-01827ce3b0bf",
        "name": "智慧农业综合管理元应用",
        "attribute": "paid",
        "type": "meta",
        "domain": "agriculture",
        "industry": "4",
        "scenario": "4",
        "technology": "计算机视觉、时序分析与预测、多模态融合（智慧种植/精准播种、病虫害防治、智能灌溉、产量预测）",
        "network": "host",
        "port": "0.0.0.0:9010/TCP → 0.0.0.0:9010",
        "volume": "/var/opt/gitlab/mnt/user → /appdata/agriculture/meta",
        "status": "released",
        "number": 512,
        "deleted": 0,
        "create_time": 1744635999646,
        "creator_id": ""
    },
    {
        "id": "ac7a408b-f01c-4565-b73f-fedc8b01a0e3",
        "name": "飞行路径规划微服务",
        "attribute": "open_source",
        "type": "atomic",
        "domain": "evtol",
        "industry": "0",
        "scenario": "0",
        "technology": "0",
        "network": "bridge",
        "port": "0.0.0.0:8200/TCP → 0.0.0.0:82000",
        "volume": "/var/opt/gitlab/mnt/user  →  /appdata/evtol/data",
        "status": "released",
        "number": 256,
        "deleted": 0,
        "create_time": 1744635999651,
        "creator_id": ""
    },
    {
        "id": "b10e3b56-9f2d-43ff-a14f-fb89810d3557",
        "name": "环境感知微服务",
        "attribute": "open_source",
        "type": "atomic",
        "domain": "evtol",
        "industry": "0",
        "scenario": "3",
        "technology": "1",
        "network": "bridge",
        "port": "0.0.0.0:8201/TCP → 0.0.0.0:82001",
        "volume": "/var/opt/gitlab/mnt/user  →  /appdata/evtol/data",
        "status": "released",
        "number": 512,
        "deleted": 0,
        "create_time": 1744635999651,
        "creator_id": ""
    },
    {
        "id": "94c085b9-fc0e-4c5b-830f-e97d7d54ede6",
        "name": "飞行控制微服务",
        "attribute": "non_intelligent",
        "type": "atomic",
        "domain": "evtol",
        "industry": "0",
        "scenario": "2",
        "technology": "0",
        "network": "bridge",
        "port": "0.0.0.0:8202/TCP → 0.0.0.0:82002",
        "volume": "/var/opt/gitlab/mnt/user  →  /appdata/evtol/data",
        "status": "released",
        "number": 256,
        "deleted": 0,
        "create_time": 1744635999651,
        "creator_id": ""
    },
    {
        "id": "49e9dd74-e61e-4d21-854d-94fe91d8ddd8",
        "name": "能源管理微服务",
        "attribute": "paid",
        "type": "atomic",
        "domain": "evtol",
        "industry": "0",
        "scenario": "4",
        "technology": "3",
        "network": "bridge",
        "port": "0.0.0.0:8203/TCP → 0.0.0.0:82003",
        "volume": "/var/opt/gitlab/mnt/user  →  /appdata/evtol/data",
        "status": "released",
        "number": 128,
        "deleted": 0,
        "create_time": 1744635999651,
        "creator_id": ""
    },
    {
        "id": "46b8c837-2450-4b87-9b41-d91242f51803",
        "name": "安全监控微服务",
        "attribute": "open_source",
        "type": "atomic",
        "domain": "evtol",
        "industry": "2",
        "scenario": "3",
        "technology": "4",
        "network": "bridge",
        "port": "0.0.0.0:8204/TCP → 0.0.0.0:82004",
        "volume": "/var/opt/gitlab/mnt/user  →  /appdata/evtol/data",
        "status": "released",
        "number": 384,
        "deleted": 0,
        "create_time": 1744635999651,
        "creator_id": ""
    },
    {
        "id": "264342fa-649d-47f9-b589-41f0c592ea14",
        "name": "eVTOL智能飞行控制元应用",
        "attribute": "open_source",
        "type": "meta",
        "domain": "evtol",
        "industry": "0",
        "scenario": "0",
        "technology": "0",
        "network": "bridge",
        "port": "0.0.0.0:8220/TCP → 0.0.0.0:82200",
        "volume": "/var/opt/gitlab/mnt/user  →  /appdata/evtol/metaApp",
        "status": "released",
        "number": 1024,
        "deleted": 0,
        "create_time": 1744635999651,
        "creator_id": ""
    },
    {
        "id": "334d0e8d-dcfe-4f7f-a41e-eb3989147a2a",
        "name": "多语言内容生成微服务",
        "attribute": "open_source",
        "type": "atomic",
        "domain": "ecommerce",
        "industry": "0",
        "scenario": "0",
        "technology": "0",
        "network": "bridge",
        "port": "0.0.0.0:8500/TCP → 0.0.0.0:85000",
        "volume": "/var/opt/gitlab/mnt/user  →  /appdata/ecommerce/data",
        "status": "released",
        "number": 256,
        "deleted": 0,
        "create_time": 1744635999654,
        "creator_id": ""
    },
    {
        "id": "9bd7eb41-81a0-48bf-bfdb-b7f6e7eb33d5",
        "name": "市场分析微服务",
        "attribute": "open_source",
        "type": "atomic",
        "domain": "ecommerce",
        "industry": "0",
        "scenario": "3",
        "technology": "3",
        "network": "bridge",
        "port": "0.0.0.0:8501/TCP → 0.0.0.0:85001",
        "volume": "/var/opt/gitlab/mnt/user  →  /appdata/ecommerce/data",
        "status": "released",
        "number": 384,
        "deleted": 0,
        "create_time": 1744635999654,
        "creator_id": ""
    },
    {
        "id": "0969a474-c3b2-4ddf-99e9-61c3ec4fb076",
        "name": "跨境电商智能营销元应用",
        "attribute": "open_source",
        "type": "meta",
        "domain": "ecommerce",
        "industry": "0",
        "scenario": "0",
        "technology": "0",
        "network": "bridge",
        "port": "0.0.0.0:8600/TCP → 0.0.0.0:86000",
        "volume": "/var/opt/gitlab/mnt/user  →  /appdata/ecommerce/meta",
        "status": "released",
        "number": 512,
        "deleted": 0,
        "create_time": 1744635999654,
        "creator_id": ""
    },
    {
        "id": "5290d2a8-777d-4cfa-8ddb-39568bcc25f3",
        "name": "环境感知微服务",
        "attribute": "open_source",
        "type": "atomic",
        "domain": "homeAI",
        "industry": "0",
        "scenario": "0",
        "technology": "0",
        "network": 5,
        "port": 4,
        "volume": 4,
        "status": "released",
        "number": 5,
        "deleted": 0,
        "create_time": 1744635999658,
        "creator_id": ""
    },
    {
        "id": "57260e5e-66d0-4d56-8281-a28ee3d550ab",
        "name": "智能对话微服务",
        "attribute": "paid",
        "type": "atomic",
        "domain": "homeAI",
        "industry": "0",
        "scenario": "0",
        "technology": "1",
        "network": 4,
        "port": 3,
        "volume": 5,
        "status": "released",
        "number": 6,
        "deleted": 0,
        "create_time": 1744635999658,
        "creator_id": ""
    },
    {
        "id": "88a6773d-7274-4071-87df-d4763855f899",
        "name": "健康监测微服务",
        "attribute": "open_source",
        "type": "atomic",
        "domain": "homeAI",
        "industry": "1",
        "scenario": "1",
        "technology": "3",
        "network": 3,
        "port": 3,
        "volume": 4,
        "status": "released",
        "number": 4,
        "deleted": 0,
        "create_time": 1744635999659,
        "creator_id": ""
    },
    {
        "id": "845f73ed-f998-4e3b-b3f1-74dbdb93a34e",
        "name": "家务辅助微服务",
        "attribute": "non_intelligent",
        "type": "atomic",
        "domain": "aml",
        "industry": "4",
        "scenario": "0",
        "technology": "2",
        "network": 4,
        "port": 3,
        "volume": 3,
        "status": "released",
        "number": 3,
        "deleted": 0,
        "create_time": 1744635999659,
        "creator_id": ""
    },
    {
        "id": "0247718c-34c6-46b7-9a75-abd4b8e615af",
        "name": "家庭智能助手元应用",
        "attribute": "open_source",
        "type": "meta",
        "domain": "homeAI",
        "industry": "0",
        "scenario": "4",
        "technology": "5",
        "network": 5,
        "port": 5,
        "volume": 5,
        "status": "released",
        "number": 1,
        "deleted": 0,
        "create_time": 1744635999659,
        "creator_id": ""
    },
]

# MOCK_SERVICE_NORMS 数据
MOCK_SERVICE_NORMS = [
    {
        "id": "27203121-5787-455c-8a56-cc4da52e48aa",
        "service_id": "3b3d4e4d-36e4-4436-bea1-63af2117d0bc",
        "key": "safety-fingerprint",
        "score": 5
    },
    {
        "id": "7981a16c-b0d3-4193-aa43-06f94ad328fb",
        "service_id": "3b3d4e4d-36e4-4436-bea1-63af2117d0bc",
        "key": "privacy",
        "score": 5
    },
    {
        "id": "41c84a36-8461-4801-abf5-62826c073638",
        "service_id": "4fda9469-dcd7-4032-affb-9c9df0cd2cc6",
        "key": "safety-fingerprint",
        "score": 5
    },{
        "id": "5f7e2bd9-a317-42c5-9d82-8a43f5c27b14",
        "service_id": "4fda9469-dcd7-4032-affb-9c9df0cd2cc6",
        "key": "safety-watermark",
        "score": 5
    },
    {
        "id": "a14ef151-2d32-492e-8599-695d0623aa57",
        "service_id": "4fda9469-dcd7-4032-affb-9c9df0cd2cc6",
        "key": "privacy",
        "score": 5
    },
    {
        "id": "7c6d1e48-f592-4639-b058-ce94a12d8f73",
        "service_id": "4fda9469-dcd7-4032-affb-9c9df0cd2cc6",
        "key": "fairness",
        "score": 5
    },
    {
        "id": "0c261206-0413-4d18-b772-7f6fb3c16314",
        "service_id": "dce40ba0-b5bb-4508-bd09-38a95a2e2932",
        "key": "robustness",
        "score": 5
    },
    {
        "id": "a119cd0c-ea54-4b97-8636-27ca153ffd29",
        "service_id": "dce40ba0-b5bb-4508-bd09-38a95a2e2932",
        "key": "privacy",
        "score": 5
    },
    {
        "id": "2a8b3c9d-e517-49f6-84a0-1b2c3d4e5f67",
        "service_id": "dce40ba0-b5bb-4508-bd09-38a95a2e2932",
        "key": "fairness",
        "score": 5
    },
    {
        "id": "7c750fb1-9e6f-4d7f-b151-7ab5323b9bed",
        "service_id": "01a951d1-09b1-4d65-9f6c-cf048e5f620e",
        "key": "safety-watermark",
        "score": 5
    },
    {
        "id": "e7c8d209-94fe-434a-bee6-fa4968571f63",
        "service_id": "01a951d1-09b1-4d65-9f6c-cf048e5f620e",
        "key": "robustness",
        "score": 5
    },
    {
        "id": "7e5113e4-4422-452f-a657-7052091d21bb",
        "service_id": "01a951d1-09b1-4d65-9f6c-cf048e5f620e",
        "key": "explainability",
        "score": 5
    },
    {
        "id": "d3973774-b4d2-4de7-aafc-3b9c2c7906e9",
        "service_id": "fde67dc7-39a2-4378-a5fe-ceec617d802f",
        "key": "robustness",
        "score": 5
    },
    {
        "id": "3f2e1d0c-b9a8-4765-98f0-12e34d56c78a",
        "service_id": "fde67dc7-39a2-4378-a5fe-ceec617d802f",
        "key": "fairness",
        "score": 5
    },
    {
        "id": "84dfba8d-960b-4b80-a805-2b58514d0fd7",
        "service_id": "fde67dc7-39a2-4378-a5fe-ceec617d802f",
        "key": "privacy",
        "score": 5
    },
    {
        "id": "2231c15e-bac0-4621-81aa-6b3c3eb1eb57",
        "service_id": "fde67dc7-39a2-4378-a5fe-ceec617d802f",
        "key": "explainability",
        "score": 5
    },
    {
        "id": "e05629f0-96e9-475e-93bd-6d41b2c287ac",
        "service_id": "1f464c6b-6b49-4fa2-8ec9-6942815f7d8f",
        "key": "safety-fingerprint",
        "score": 5
    },
    {
        "id": "7161e1d8-2dc4-4e78-b669-af72694aeff1",
        "service_id": "1f464c6b-6b49-4fa2-8ec9-6942815f7d8f",
        "key": "robustness",
        "score": 5
    },
    {
        "id": "b293cb0b-626a-43d2-95f9-b0c090e86267",
        "service_id": "1f464c6b-6b49-4fa2-8ec9-6942815f7d8f",
        "key": "privacy",
        "score": 5
    },
    {
        "id": "25e2137b-4167-42d6-9b51-410c0e8338f4",
        "service_id": "b352ae47-92db-4281-8faf-9491ab6baea3",
        "key": "robustness",
        "score": 5
    },
    {
        "id": "92af12b6-0a5e-4fd6-b218-b26b444bc519",
        "service_id": "b352ae47-92db-4281-8faf-9491ab6baea3",
        "key": "privacy",
        "score": 5
    },
    {
        "id": "493fda23-6ea6-48e0-901d-e1ecb0d68c5e",
        "service_id": "b352ae47-92db-4281-8faf-9491ab6baea3",
        "key": "explainability",
        "score": 5
    },
    {
        "id": "2ba5a42e-301c-406c-b18a-79995d3ddd22",
        "service_id": "c482ad98-4a7b-4498-a4d5-a52f991d1c0d",
        "key": "robustness",
        "score": 5
    },
    {
        "id": "5c0f15d8-4974-4759-9a50-9c9f49d73e4b",
        "service_id": "c482ad98-4a7b-4498-a4d5-a52f991d1c0d",
        "key": "privacy",
        "score": 5
    },
    {
        "id": "e48498df-6f7c-4d1f-bc54-945b596746e7",
        "service_id": "c482ad98-4a7b-4498-a4d5-a52f991d1c0d",
        "key": "explainability",
        "score": 5
    },
    {
        "id": "03d00783-4904-47a2-ba88-58edbd65eae4",
        "service_id": "b1b8417a-145c-43e3-b0d1-1aa3d7279c6b",
        "key": "safety-fingerprint",
        "score": 5
    },
    {
        "id": "01789004-8cb5-410e-9706-cc0b4038f666",
        "service_id": "b1b8417a-145c-43e3-b0d1-1aa3d7279c6b",
        "key": "robustness",
        "score": 5
    },
    {
        "id": "7988b3d2-0a00-4096-9a3f-e7e5d9688894",
        "service_id": "b1b8417a-145c-43e3-b0d1-1aa3d7279c6b",
        "key": "privacy",
        "score": 5
    },
    {
        "id": "2715e0f3-9eb1-4c9d-ba15-35a883ea02f1",
        "service_id": "b1b8417a-145c-43e3-b0d1-1aa3d7279c6b",
        "key": "explainability",
        "score": 5
    },
    {
        "id": "6eb2e8de-3c3f-4aa9-b6a4-7c66bf21ad94",
        "service_id": "3c93a110-4618-4b12-83fd-4b5a6f89a105",
        "key": "safety-fingerprint",
        "score": 5
    },
    {
        "id": "9e8d7c6b-5a4f-4321-b0a9-87f6e5d4c3b2",
        "service_id": "3c93a110-4618-4b12-83fd-4b5a6f89a105",
        "key": "safety-watermark",
        "score": 5
    },
    {
        "id": "de6176af-1eb3-42b5-9d2c-85fe689aeeb1",
        "service_id": "3c93a110-4618-4b12-83fd-4b5a6f89a105",
        "key": "robustness",
        "score": 5
    },
    {
        "id": "fb9fc9e4-0bde-4185-811a-607d8a2f9eca",
        "service_id": "3c93a110-4618-4b12-83fd-4b5a6f89a105",
        "key": "privacy",
        "score": 5
    },
    {
        "id": "ed382894-ec9d-4a07-8401-23ce26083630",
        "service_id": "77064ca6-3a5d-49cd-8a27-c6a7b52fc20e",
        "key": "safety-fingerprint",
        "score": 5
    },
    {
        "id": "18efc7f0-11c1-4e52-af1f-fc62c879d522",
        "service_id": "77064ca6-3a5d-49cd-8a27-c6a7b52fc20e",
        "key": "privacy",
        "score": 5
    },
    {
        "id": "c5a16ce5-8d06-4c3f-9a41-74c35a62d097",
        "service_id": "74e5ff68-23a9-4109-967d-a5a76f29ba6a",
        "key": "robustness",
        "score": 5
    },
    {
        "id": "33b491f1-1535-48ae-bc5a-3705d361bcde",
        "service_id": "74e5ff68-23a9-4109-967d-a5a76f29ba6a",
        "key": "privacy",
        "score": 5
    },
    {
        "id": "613ae4ae-6b8b-4980-907f-00fa958a867d",
        "service_id": "da43a293-fb67-4efb-b65b-ec22d9cca5ae",
        "key": "safety-fingerprint",
        "score": 5
    },
    {
        "id": "d919aa64-ae29-4cbc-8b98-c557d9ce26c7",
        "service_id": "da43a293-fb67-4efb-b65b-ec22d9cca5ae",
        "key": "robustness",
        "score": 5
    },
    {
        "id": "10975b41-5bb8-403f-b57b-906799295c56",
        "service_id": "da43a293-fb67-4efb-b65b-ec22d9cca5ae",
        "key": "explainability",
        "score": 5
    },
    {
        "id": "179961bc-5ad7-4cb4-a2df-c68cb2780d4a",
        "service_id": "aacc5100-a017-49d9-a784-c7fe210d234c",
        "key": "robustness",
        "score": 5
    },
    {
        "id": "caf0f0a7-8927-4d29-962a-d8f1e20ffa22",
        "service_id": "aacc5100-a017-49d9-a784-c7fe210d234c",
        "key": "privacy",
        "score": 5
    },
    {
        "id": "1b2be93e-1c82-4eb2-808e-2bef6cd04e84",
        "service_id": "aacc5100-a017-49d9-a784-c7fe210d234c",
        "key": "explainability",
        "score": 5
    },
    {
        "id": "9fb131d2-0d21-46e1-9b89-639b7756b006",
        "service_id": "57b897b2-f191-4ede-98d6-46aaee8bd4e8",
        "key": "safety-fingerprint",
        "score": 5
    },
    {
        "id": "2e545236-6ace-4434-8ced-dfcfaca6393d",
        "service_id": "57b897b2-f191-4ede-98d6-46aaee8bd4e8",
        "key": "robustness",
        "score": 5
    },
    {
        "id": "69dd1da1-b134-4749-9fb7-f72a18326847",
        "service_id": "57b897b2-f191-4ede-98d6-46aaee8bd4e8",
        "key": "privacy",
        "score": 5
    },
    {
        "id": "887f1daf-39ac-4dd4-a7e8-18c0983fb7cb",
        "service_id": "57b897b2-f191-4ede-98d6-46aaee8bd4e8",
        "key": "explainability",
        "score": 5
    },
    {
        "id": "2a28f619-33c5-43bf-b535-d83e3e9ec72a",
        "service_id": "fa3fafbb-fb30-492d-93cf-b608e06b4d99",
        "key": "safety-fingerprint",
        "score": 5
    },
    {
        "id": "5cc948bc-ca7d-4e45-9f56-7eb2cbde7d54",
        "service_id": "fa3fafbb-fb30-492d-93cf-b608e06b4d99",
        "key": "privacy",
        "score": 5
    },
    {
        "id": "027020a4-b9c8-41ae-bd71-3d3c3bd63a7d",
        "service_id": "f6c3c542-59ed-4277-b771-21f5191d8c5c",
        "key": "safety-fingerprint",
        "score": 5
    },
    {
        "id": "a8e6d0be-eb60-4090-86d3-e697a5a72f84",
        "service_id": "f6c3c542-59ed-4277-b771-21f5191d8c5c",
        "key": "privacy",
        "score": 4
    },
    {
        "id": "4ed23871-e10a-4246-bfc4-41405914a50e",
        "service_id": "fd918206-0564-408b-a096-efd3b64c4efc",
        "key": "robustness",
        "score": 4
    },
    {
        "id": "e98a07db-8919-4cad-9a13-b31d618e9130",
        "service_id": "fd918206-0564-408b-a096-efd3b64c4efc",
        "key": "explainability",
        "score": 5
    },
    {
        "id": "e12b9260-8b73-4048-b182-e17211fbd4f1",
        "service_id": "e54ba826-ad95-45aa-928a-cea6d2d94e2a",
        "key": "robustness",
        "score": 5
    },
    {
        "id": "8f1ff9eb-0166-43f2-ac78-121f848cf33c",
        "service_id": "e54ba826-ad95-45aa-928a-cea6d2d94e2a",
        "key": "privacy",
        "score": 4
    },
    {
        "id": "7608ef8c-55ee-4ad6-8330-0f9e95b8b4ed",
        "service_id": "957f8b36-d0c7-462a-9041-cfb2e063f328",
        "key": "safety-fingerprint",
        "score": 4
    },
    {
        "id": "64a0cb4a-c21d-45ea-bfc7-34faa6d96302",
        "service_id": "957f8b36-d0c7-462a-9041-cfb2e063f328",
        "key": "explainability",
        "score": 5
    },
    {
        "id": "e70c50c1-4d17-4c79-b3c3-c46280a589b4",
        "service_id": "cd670e2a-8567-437d-8dd2-27eee559be19",
        "key": "robustness",
        "score": 5
    },
    {
        "id": "22fa925d-2f75-4da7-9478-5960b1d876cd",
        "service_id": "cd670e2a-8567-437d-8dd2-27eee559be19",
        "key": "explainability",
        "score": 5
    },
    {
        "id": "58079a6c-ab7d-4e31-ab28-9ae9e763ce3b",
        "service_id": "fa4c11e8-e76a-49c5-903a-9634dc3abe67",
        "key": "safety-fingerprint",
        "score": 5
    },
    {
        "id": "d60870d0-3984-4491-9968-3385b4a0d9a4",
        "service_id": "fa4c11e8-e76a-49c5-903a-9634dc3abe67",
        "key": "robustness",
        "score": 4
    },
    {
        "id": "73b9f11d-c857-4664-98bf-4ffbafe7b019",
        "service_id": "fa4c11e8-e76a-49c5-903a-9634dc3abe67",
        "key": "privacy",
        "score": 5
    },
    {
        "id": "95c47236-96c8-440c-93b5-32f54f396883",
        "service_id": "fa4c11e8-e76a-49c5-903a-9634dc3abe67",
        "key": "explainability",
        "score": 5
    },
    {
        "id": "1863998c-4de9-4f44-acbb-2b98ad745e1d",
        "service_id": "80b3b5e1-f2bc-4cd2-a196-0298aa8cc57a",
        "key": "safety-fingerprint",
        "score": 4
    },
    {
        "id": "cd4a69ae-8164-4cea-996c-69d69d5d1412",
        "service_id": "80b3b5e1-f2bc-4cd2-a196-0298aa8cc57a",
        "key": "robustness",
        "score": 5
    },
    {
        "id": "2d0f8165-470f-488e-b45c-94e1148541ed",
        "service_id": "80b3b5e1-f2bc-4cd2-a196-0298aa8cc57a",
        "key": "privacy",
        "score": 4
    },
    {
        "id": "31d2ec1a-4924-43ab-8ebe-b3857dbd13c2",
        "service_id": "80b3b5e1-f2bc-4cd2-a196-0298aa8cc57a",
        "key": "explainability",
        "score": 5
    },
    {
        "id": "4f90a300-78a8-4b4a-aea6-eee7a3403174",
        "service_id": "4f35b674-4a5b-4b69-a55c-ef0a0ccf2553",
        "key": "safety-fingerprint",
        "score": 5
    },
    {
        "id": "e52d9068-438f-4c35-bcbc-112425551e7d",
        "service_id": "4f35b674-4a5b-4b69-a55c-ef0a0ccf2553",
        "key": "privacy",
        "score": 4
    },
    {
        "id": "06546963-9dfb-4c5e-9b54-a6170f0dfd80",
        "service_id": "f6be78dc-ac2b-485f-93ec-0f7215797d21",
        "key": "safety-fingerprint",
        "score": 5
    },
    {
        "id": "6ff1a3e2-3f94-4a17-8445-fc144a26d687",
        "service_id": "f6be78dc-ac2b-485f-93ec-0f7215797d21",
        "key": "privacy",
        "score": 5
    },
    {
        "id": "64181cc3-bb6d-469e-ae49-210df869d21e",
        "service_id": "c5f36a0f-888f-4900-b970-890b13bc0e86",
        "key": "safety-fingerprint",
        "score": 4
    },
    {
        "id": "7b117107-fe05-4afb-8eaa-03aa14cdc04d",
        "service_id": "c5f36a0f-888f-4900-b970-890b13bc0e86",
        "key": "privacy",
        "score": 5
    },
    {
        "id": "8c2e7dd4-8dd2-4e19-8bbc-c12c79b3a286",
        "service_id": "241009ad-8465-44a8-befb-bfb9c000c2cb",
        "key": "safety-fingerprint",
        "score": 4
    },
    {
        "id": "32ab8c38-125b-4ce5-9076-692d8d9ec808",
        "service_id": "241009ad-8465-44a8-befb-bfb9c000c2cb",
        "key": "privacy",
        "score": 4
    },
    {
        "id": "5f9e4029-eae3-4fc3-8f7f-b89b64051c15",
        "service_id": "9fe9c51a-aa30-44b0-95ff-01827ce3b0bf",
        "key": "safety-fingerprint",
        "score": 5
    },
    {
        "id": "7e24dd96-4fe8-487e-8378-42f3e2e2ee2f",
        "service_id": "9fe9c51a-aa30-44b0-95ff-01827ce3b0bf",
        "key": "privacy",
        "score": 5
    },
    {
        "id": "b1222b86-88ef-47c0-aed5-07aee391e9eb",
        "service_id": "ac7a408b-f01c-4565-b73f-fedc8b01a0e3",
        "key": "safety-fingerprint",
        "score": 5
    },
    {
        "id": "aca78f9b-acec-4169-b7cc-5e2db04f9e39",
        "service_id": "ac7a408b-f01c-4565-b73f-fedc8b01a0e3",
        "key": "privacy",
        "score": 5
    },
    {
        "id": "2bb2b4c0-4d2c-4cb5-af90-9c4b30189991",
        "service_id": "b10e3b56-9f2d-43ff-a14f-fb89810d3557",
        "key": "robustness",
        "score": 5
    },
    {
        "id": "e43f8b9e-566e-488e-a67d-3beb6a1112dd",
        "service_id": "b10e3b56-9f2d-43ff-a14f-fb89810d3557",
        "key": "explainability",
        "score": 4
    },
    {
        "id": "15883807-61d2-4f20-baea-e58bd48b38c3",
        "service_id": "94c085b9-fc0e-4c5b-830f-e97d7d54ede6",
        "key": "safety-fingerprint",
        "score": 5
    },
    {
        "id": "9404d775-3f23-4168-95fe-2f3cee735286",
        "service_id": "94c085b9-fc0e-4c5b-830f-e97d7d54ede6",
        "key": "robustness",
        "score": 5
    },
    {
        "id": "45ad97d8-dc77-4633-b065-d2a4ee2fde59",
        "service_id": "94c085b9-fc0e-4c5b-830f-e97d7d54ede6",
        "key": "privacy",
        "score": 5
    },
    {
        "id": "102cf40f-8c70-4242-bc0c-96cd36443b95",
        "service_id": "49e9dd74-e61e-4d21-854d-94fe91d8ddd8",
        "key": "safety-fingerprint",
        "score": 4
    },
    {
        "id": "8b4746ca-1c4f-410d-8680-2d973330971b",
        "service_id": "49e9dd74-e61e-4d21-854d-94fe91d8ddd8",
        "key": "explainability",
        "score": 5
    },
    {
        "id": "44391ee6-5053-4851-bfab-eb74ef9e132a",
        "service_id": "46b8c837-2450-4b87-9b41-d91242f51803",
        "key": "robustness",
        "score": 5
    },
    {
        "id": "d099b806-94f2-41f2-a52e-224181eeae9a",
        "service_id": "46b8c837-2450-4b87-9b41-d91242f51803",
        "key": "privacy",
        "score": 4
    },
    {
        "id": "da78439c-7d27-4bc2-8ec6-57bd4541bde5",
        "service_id": "46b8c837-2450-4b87-9b41-d91242f51803",
        "key": "explainability",
        "score": 5
    },
    {
        "id": "221109b5-b6fe-41a0-b011-fa53b564e80a",
        "service_id": "264342fa-649d-47f9-b589-41f0c592ea14",
        "key": "safety-fingerprint",
        "score": 5
    },
    {
        "id": "fea2dc46-81a9-4a36-b133-3c291a782273",
        "service_id": "264342fa-649d-47f9-b589-41f0c592ea14",
        "key": "robustness",
        "score": 5
    },
    {
        "id": "725beead-6b88-4ee1-b40c-66f5c22408fe",
        "service_id": "264342fa-649d-47f9-b589-41f0c592ea14",
        "key": "privacy",
        "score": 5
    },
    {
        "id": "cec57c30-5853-4792-8960-ff9d29d22497",
        "service_id": "264342fa-649d-47f9-b589-41f0c592ea14",
        "key": "explainability",
        "score": 5
    },
    {
        "id": "6e46a0b7-be85-4a79-bd65-a104ec4ecfa8",
        "service_id": "334d0e8d-dcfe-4f7f-a41e-eb3989147a2a",
        "key": "safety-fingerprint",
        "score": 5
    },
    {
        "id": "e0eef67e-97b8-4695-a24f-6f72d5b949ec",
        "service_id": "334d0e8d-dcfe-4f7f-a41e-eb3989147a2a",
        "key": "robustness",
        "score": 5
    },
    {
        "id": "75f934a2-8ed4-44f0-8fe0-78f37329e878",
        "service_id": "334d0e8d-dcfe-4f7f-a41e-eb3989147a2a",
        "key": "privacy",
        "score": 5
    },
    {
        "id": "80af7db5-f542-4cb7-9d22-08e9d99bcc91",
        "service_id": "334d0e8d-dcfe-4f7f-a41e-eb3989147a2a",
        "key": "explainability",
        "score": 5
    },
    {
        "id": "913d0d22-100c-49f0-85ac-f500972bf1f3",
        "service_id": "9bd7eb41-81a0-48bf-bfdb-b7f6e7eb33d5",
        "key": "safety-fingerprint",
        "score": 5
    },
    {
        "id": "a5ca8dcf-bf6a-4f57-a768-0fc74d4c6cb9",
        "service_id": "9bd7eb41-81a0-48bf-bfdb-b7f6e7eb33d5",
        "key": "privacy",
        "score": 5
    },
    {
        "id": "ee478388-3878-47f1-9ee6-8faa659625a2",
        "service_id": "9bd7eb41-81a0-48bf-bfdb-b7f6e7eb33d5",
        "key": "explainability",
        "score": 5
    },
    {
        "id": "45134a7b-0041-4c22-bd9c-b4cefc052e9b",
        "service_id": "0969a474-c3b2-4ddf-99e9-61c3ec4fb076",
        "key": "safety-fingerprint",
        "score": 5
    },
    {
        "id": "e1279006-4d42-4fa1-b9e5-901c677b3c87",
        "service_id": "0969a474-c3b2-4ddf-99e9-61c3ec4fb076",
        "key": "robustness",
        "score": 5
    },
    {
        "id": "4fe82efb-d413-4729-ab79-95327f4a0235",
        "service_id": "0969a474-c3b2-4ddf-99e9-61c3ec4fb076",
        "key": "explainability",
        "score": 5
    },
    {
        "id": "845c5890-3024-44a1-8083-c6cdf0779356",
        "service_id": "5290d2a8-777d-4cfa-8ddb-39568bcc25f3",
        "key": "safety-fingerprint",
        "score": 5
    },
    {
        "id": "05358bb0-3d13-4179-a7d3-f8895a80c801",
        "service_id": "5290d2a8-777d-4cfa-8ddb-39568bcc25f3",
        "key": "robustness",
        "score": 5
    },
    {
        "id": "37c6fa2e-99d6-4009-b311-bac6c171e949",
        "service_id": "5290d2a8-777d-4cfa-8ddb-39568bcc25f3",
        "key": "privacy",
        "score": 5
    },
    {
        "id": "d4c9fb77-f8dc-4820-b262-dc97372b0b2f",
        "service_id": "5290d2a8-777d-4cfa-8ddb-39568bcc25f3",
        "key": "explainability",
        "score": 5
    },
    {
        "id": "c2333bf2-841e-4dff-9d3e-aab7c5d923cd",
        "service_id": "57260e5e-66d0-4d56-8281-a28ee3d550ab",
        "key": "safety-fingerprint",
        "score": 5
    },
    {
        "id": "7634a0c7-2db7-4393-a916-fd4ef84a1a6e",
        "service_id": "57260e5e-66d0-4d56-8281-a28ee3d550ab",
        "key": "robustness",
        "score": 5
    },
    {
        "id": "e828849c-897a-430e-ab37-7efe91dc0e21",
        "service_id": "57260e5e-66d0-4d56-8281-a28ee3d550ab",
        "key": "privacy",
        "score": 5
    },
    {
        "id": "9e2d5d2f-a262-4c97-884c-c0d7e1b0b381",
        "service_id": "57260e5e-66d0-4d56-8281-a28ee3d550ab",
        "key": "explainability",
        "score": 5
    },
    {
        "id": "7e8b6a0b-d56f-4d05-93cc-3e5b65445977",
        "service_id": "88a6773d-7274-4071-87df-d4763855f899",
        "key": "robustness",
        "score": 5
    },
    {
        "id": "12ddf278-4f1c-42e7-827d-15c4975838cd",
        "service_id": "88a6773d-7274-4071-87df-d4763855f899",
        "key": "privacy",
        "score": 5
    },
    {
        "id": "aa5c3d3b-4721-4dec-b482-456938f55863",
        "service_id": "88a6773d-7274-4071-87df-d4763855f899",
        "key": "explainability",
        "score": 5
    },
    {
        "id": "c48d31ec-ee21-46eb-b43d-65f8541488a3",
        "service_id": "845f73ed-f998-4e3b-b3f1-74dbdb93a34e",
        "key": "safety-fingerprint",
        "score": 5
    },
    {
        "id": "957afb08-2ab7-4bc4-a17e-44e8854532ae",
        "service_id": "845f73ed-f998-4e3b-b3f1-74dbdb93a34e",
        "key": "privacy",
        "score": 5
    },
    {
        "id": "e55aacf6-be15-496a-bf33-89cd2d551016",
        "service_id": "845f73ed-f998-4e3b-b3f1-74dbdb93a34e",
        "key": "explainability",
        "score": 5
    },
    {
        "id": "87c1fa43-a229-48b8-9f19-8764b0f519ca",
        "service_id": "0247718c-34c6-46b7-9a75-abd4b8e615af",
        "key": "safety-fingerprint",
        "score": 5
    },
    {
        "id": "1aa41c26-68f2-424b-a2a9-9eefa3e2bb1d",
        "service_id": "0247718c-34c6-46b7-9a75-abd4b8e615af",
        "key": "robustness",
        "score": 5
    },
    {
        "id": "b12af483-ae11-4b13-b4b6-31e5094bdc89",
        "service_id": "0247718c-34c6-46b7-9a75-abd4b8e615af",
        "key": "privacy",
        "score": 5
    },
]

# MOCK_SERVICE_SOURCES 数据
MOCK_SERVICE_SOURCES = [
    {
        "id": "4f4cce6b-d79c-4e49-958e-023b443c864b",
        "service_id": "3b3d4e4d-36e4-4436-bea1-63af2117d0bc",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "课题一",
        "ms_introduce": "基于智能体的风险识别算法",
        "company_score": 5,
        "ms_score": 5
    },
    {
        "id": "ae173ff3-23e2-4133-b5d2-ddf1d4407d44",
        "service_id": "4fda9469-dcd7-4032-affb-9c9df0cd2cc6",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "课题二",
        "ms_introduce": "基于多方安全计算的风险识别算法",
        "company_score": 5,
        "ms_score": 5
    },
    {
        "id": "6ea04e39-06dd-462f-8625-26f33c224cf8",
        "service_id": "dce40ba0-b5bb-4508-bd09-38a95a2e2932",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "课题五",
        "ms_introduce": "课题五样例服务",
        "company_score": 5,
        "ms_score": 5
    },
    {
        "id": "94de8c76-1e69-4772-ab37-770c7de4ac85",
        "service_id": "01a951d1-09b1-4d65-9f6c-cf048e5f620e",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "课题一",
        "ms_introduce": "简易版报告生成",
        "company_score": 5,
        "ms_score": 5
    },
    {
        "id": "ed2ec310-b9bf-4946-ac4a-41df7176a3f0",
        "service_id": "fde67dc7-39a2-4378-a5fe-ceec617d802f",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "课题五",
        "ms_introduce": "课题五样例服务",
        "company_score": 5,
        "ms_score": 5
    },
    {
        "id": "7c7796a2-7765-4018-aaec-5223fb070345",
        "service_id": "1f464c6b-6b49-4fa2-8ec9-6942815f7d8f",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "课题五",
        "ms_introduce": "课题五AI技术中台上传、发布算法样例服务",
        "company_score": 5,
        "ms_score": 5
    },
    {
        "id": "713103c8-c850-4345-bcb8-f901ae1a8c0c",
        "service_id": "b352ae47-92db-4281-8faf-9491ab6baea3",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "课题三",
        "ms_introduce": "金融风险报告生成",
        "company_score": 5,
        "ms_score": 5
    },
    {
        "id": "30ac0e10-e238-453d-a915-2a4f53104473",
        "service_id": "c482ad98-4a7b-4498-a4d5-a52f991d1c0d",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "课题四",
        "ms_introduce": "安全性指纹测评算法",
        "company_score": 5,
        "ms_score": 5
    },
    {
        "id": "887c61cb-5297-42ca-87f2-6597cbeb8fb7",
        "service_id": "b1b8417a-145c-43e3-b0d1-1aa3d7279c6b",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "课题五",
        "ms_introduce": "用于跨境支付的风险评估和报告生成的元应用样例",
        "company_score": 5,
        "ms_score": 5
    },
    {
        "id": "c58931f2-2fe3-414e-827c-71146516ab20",
        "service_id": "3c93a110-4618-4b12-83fd-4b5a6f89a105",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "课题五",
        "ms_introduce": "基于智能体的无人机虚拟仿真微服务",
        "company_score": 5,
        "ms_score": 5
    },
    {
        "id": "47edb4cd-45a7-4e92-ac19-e944857d8f97",
        "service_id": "77064ca6-3a5d-49cd-8a27-c6a7b52fc20e",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "无人机AI应用课题",
        "ms_introduce": "基于智能体的无人机低空测绘微服务",
        "company_score": 5,
        "ms_score": 5
    },
    {
        "id": "bbc3d610-3bd6-46ec-b26b-f88e695da1c4",
        "service_id": "74e5ff68-23a9-4109-967d-a5a76f29ba6a",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "无人机AI应用课题",
        "ms_introduce": "基于智能体的无人机目标识别微服务",
        "company_score": 5,
        "ms_score": 5
    },
    {
        "id": "a835a9cf-8992-4548-a65d-427953f14921",
        "service_id": "da43a293-fb67-4efb-b65b-ec22d9cca5ae",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "无人机AI应用课题",
        "ms_introduce": "基于智能体的无人机远程控制微服务",
        "company_score": 5,
        "ms_score": 5
    },
    {
        "id": "bb96def0-83d8-4671-9ef3-83ef5053991c",
        "service_id": "aacc5100-a017-49d9-a784-c7fe210d234c",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "无人机AI应用课题",
        "ms_introduce": "基于智能体的无人机视频分析微服务",
        "company_score": 5,
        "ms_score": 5
    },
    {
        "id": "d6db87d0-b0ce-45bf-b93d-fcd2afb02393",
        "service_id": "57b897b2-f191-4ede-98d6-46aaee8bd4e8",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "",
        "ms_introduce": "针对跨境贸易支付监管的误检率高、效率低问题，本课题旨在研究新的监管方法和机制，支持新时代的监管体系构建。基于高性能分布式图数据库和FIDO客户认证，通过高性能图分析算法优化规则驱动的跨境支付监管，确保数据真实性并实现高并发事中监管。",
        "company_score": 5,
        "ms_score": 5
    },
    {
        "id": "62387956-2754-4f5f-9329-676f495af122",
        "service_id": "fa3fafbb-fb30-492d-93cf-b608e06b4d99",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "药学院临床药学系",
        "ms_introduce": "基于群体药动学模型的肝移植患者利奈唑胺给药方案优化",
        "company_score": 5,
        "ms_score": 5
    },
    {
        "id": "77a90d39-4545-414b-a675-0e651ab1c935",
        "service_id": "f6c3c542-59ed-4277-b771-21f5191d8c5c",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "乡村医疗AI应用课题",
        "ms_introduce": "基于轻量化模型的医疗影像辅助诊断服务",
        "company_score": 5,
        "ms_score": 4
    },
    {
        "id": "152581d2-ece2-470e-9215-621e1f9a4f93",
        "service_id": "fd918206-0564-408b-a096-efd3b64c4efc",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "乡村医疗AI应用课题",
        "ms_introduce": "基于物联网和AI的慢性病监测服务",
        "company_score": 4,
        "ms_score": 5
    },
    {
        "id": "4627f953-748d-4c18-957c-d3ce4a7f47db",
        "service_id": "e54ba826-ad95-45aa-928a-cea6d2d94e2a",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "乡村医疗AI应用课题",
        "ms_introduce": "农村方言语音识别转写服务",
        "company_score": 4,
        "ms_score": 5
    },
    {
        "id": "f79c4fc2-9370-42c8-adb6-b8e5717cb26f",
        "service_id": "957f8b36-d0c7-462a-9041-cfb2e063f328",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "乡村医疗AI应用课题",
        "ms_introduce": "基于强化学习的医疗资源优化调度服务",
        "company_score": 5,
        "ms_score": 4
    },
    {
        "id": "63756f58-0b11-4df0-844a-5b6a17f51636",
        "service_id": "cd670e2a-8567-437d-8dd2-27eee559be19",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "乡村医疗AI应用课题",
        "ms_introduce": "基于时序数据分析的流行病预测服务",
        "company_score": 5,
        "ms_score": 5
    },
    {
        "id": "cf3e3e8f-ac04-4347-95e9-8121587ba901",
        "service_id": "fa4c11e8-e76a-49c5-903a-9634dc3abe67",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "乡村医疗AI应用课题",
        "ms_introduce": "针对基层医疗机构的AI辅助诊断元应用，整合了医学影像处理和方言语音识别功能",
        "company_score": 5,
        "ms_score": 4
    },
    {
        "id": "2ce20f46-8d33-40b1-8793-fef2b61ab7fc",
        "service_id": "80b3b5e1-f2bc-4cd2-a196-0298aa8cc57a",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "乡村医疗AI应用课题",
        "ms_introduce": "农村地区公共卫生监测元应用，整合流行病预测和医疗资源调度功能",
        "company_score": 5,
        "ms_score": 5
    },
    {
        "id": "30f62aa2-6f67-453e-88ab-9cf6a5ffc1a0",
        "service_id": "4f35b674-4a5b-4b69-a55c-ef0a0ccf2553",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "数字农业AI应用课题",
        "ms_introduce": "基于计算机视觉的农作物生长状态智能分析服务",
        "company_score": 5,
        "ms_score": 5
    },
    {
        "id": "19607a9e-4a01-4223-b313-6ac45c417288",
        "service_id": "f6be78dc-ac2b-485f-93ec-0f7215797d21",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "数字农业AI应用课题",
        "ms_introduce": "基于深度学习的病虫害智能识别与防治系统",
        "company_score": 5,
        "ms_score": 5
    },
    {
        "id": "556f5f93-c072-4efc-84e9-115eb88055bb",
        "service_id": "c5f36a0f-888f-4900-b970-890b13bc0e86",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "数字农业AI应用课题",
        "ms_introduce": "基于时序分析的农田智能灌溉决策系统",
        "company_score": 5,
        "ms_score": 4
    },
    {
        "id": "ef160187-1ecc-4418-926d-2f4d77fde4de",
        "service_id": "241009ad-8465-44a8-befb-bfb9c000c2cb",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "数字农业AI应用课题",
        "ms_introduce": "基于机器学习的农作物产量预测服务",
        "company_score": 5,
        "ms_score": 4
    },
    {
        "id": "08c41856-10c9-4d19-83cf-337c25d2262f",
        "service_id": "9fe9c51a-aa30-44b0-95ff-01827ce3b0bf",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "数字农业AI应用课题",
        "ms_introduce": "基于多代理系统的智慧农业综合管理平台",
        "company_score": 5,
        "ms_score": 5
    },
    {
        "id": "2ea9b4a3-9588-436c-a6c5-e9c8248641ab",
        "service_id": "ac7a408b-f01c-4565-b73f-fedc8b01a0e3",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "低空飞行（eVTOL）AI应用课题",
        "ms_introduce": "基于强化学习的飞行路径规划服务",
        "company_score": 5,
        "ms_score": 5
    },
    {
        "id": "1e530d6e-0967-482c-b7aa-f08432c85bad",
        "service_id": "b10e3b56-9f2d-43ff-a14f-fb89810d3557",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "低空飞行（eVTOL）AI应用课题",
        "ms_introduce": "基于计算机视觉和多传感器融合的环境感知服务",
        "company_score": 5,
        "ms_score": 4
    },
    {
        "id": "34f1a12f-6248-4f2a-9dcb-c7666d01da04",
        "service_id": "94c085b9-fc0e-4c5b-830f-e97d7d54ede6",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "低空飞行（eVTOL）AI应用课题",
        "ms_introduce": "基于PID控制算法的飞行姿态控制服务",
        "company_score": 5,
        "ms_score": 5
    },
    {
        "id": "179553a0-1e26-40d8-8e17-8eef89a04c51",
        "service_id": "49e9dd74-e61e-4d21-854d-94fe91d8ddd8",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "低空飞行（eVTOL）AI应用课题",
        "ms_introduce": "基于时序预测的电池能源管理服务",
        "company_score": 4,
        "ms_score": 5
    },
    {
        "id": "04b2c67b-b7a2-4ee3-a05c-6897e901bc3b",
        "service_id": "46b8c837-2450-4b87-9b41-d91242f51803",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "低空飞行（eVTOL）AI应用课题",
        "ms_introduce": "基于异常检测算法的飞行安全监控服务",
        "company_score": 5,
        "ms_score": 5
    },
    {
        "id": "1c30c209-f395-4c05-b8e2-0fae4d5870a4",
        "service_id": "264342fa-649d-47f9-b589-41f0c592ea14",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "低空飞行（eVTOL）AI应用课题",
        "ms_introduce": "集成了路径规划、环境感知和飞行控制的综合元应用",
        "company_score": 5,
        "ms_score": 5
    },
    {
        "id": "68b1c373-8ee8-46fe-8c34-6614f08218be",
        "service_id": "334d0e8d-dcfe-4f7f-a41e-eb3989147a2a",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "跨境电商AI应用课题",
        "ms_introduce": "垂域多语言生成大模型",
        "company_score": 5,
        "ms_score": 5
    },
    {
        "id": "e7850969-fba3-451c-8201-0783e5811255",
        "service_id": "9bd7eb41-81a0-48bf-bfdb-b7f6e7eb33d5",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "跨境电商AI应用课题",
        "ms_introduce": "基于智能体的市场分析算法",
        "company_score": 5,
        "ms_score": 5
    },
    {
        "id": "9c531368-d14e-403b-b9e0-dfdbcc34d34a",
        "service_id": "0969a474-c3b2-4ddf-99e9-61c3ec4fb076",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "跨境电商AI应用课题",
        "ms_introduce": "基于智能体的风险识别算法",
        "company_score": 5,
        "ms_score": 5
    },
    {
        "id": "8047d47e-e38c-4c79-9ac3-e25cf9f7030d",
        "service_id": "5290d2a8-777d-4cfa-8ddb-39568bcc25f3",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "家庭智能助手AI应用课题",
        "ms_introduce": "基于智能体的环境感知算法",
        "company_score": 5,
        "ms_score": 5
    },
    {
        "id": "3fa0425d-eeee-435f-99aa-fad04e97e6f1",
        "service_id": "57260e5e-66d0-4d56-8281-a28ee3d550ab",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "家庭智能助手AI应用课题",
        "ms_introduce": "基于多模态情感识别算法",
        "company_score": 5,
        "ms_score": 5
    },
    {
        "id": "793ab416-8bd2-46e3-b688-edbb6a6656d3",
        "service_id": "88a6773d-7274-4071-87df-d4763855f899",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "家庭智能助手AI应用课题",
        "ms_introduce": "基于多模态情感识别算法",
        "company_score": 5,
        "ms_score": 5
    },
    {
        "id": "19013ee0-1993-4a0d-8f25-803ab44f1598",
        "service_id": "845f73ed-f998-4e3b-b3f1-74dbdb93a34e",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "家庭智能助手AI应用课题",
        "ms_introduce": "基于强化学习的任务规划算法",
        "company_score": 5,
        "ms_score": 5
    },
    {
        "id": "14096ab0-7e2b-42aa-87ad-fa03ff97b88c",
        "service_id": "0247718c-34c6-46b7-9a75-abd4b8e615af",
        "popover_title": "可信云技术服务溯源",
        "company_name": "复旦大学课题组",
        "company_address": "上海市杨浦区邯郸路220号",
        "company_contact": "021-65642222",
        "company_introduce": "家庭智能助手AI应用课题",
        "ms_introduce": "家庭智能助手",
        "company_score": 5,
        "ms_score": 5
    },
]

# MOCK_SERVICE_APIS 数据
MOCK_SERVICE_APIS = [
    {
        "id": "1bfa846d-6fbd-4c1f-a3c9-0b476b03004e",
        "service_id": "3b3d4e4d-36e4-4436-bea1-63af2117d0bc",
        "name": "predict",
        "url": "/api/project1/predict",
        "method": "POST",
        "des": "模型推理接口，基于数据集和参数配置得到风险识别结果",
        "parameter_type": 2,
        "response_type": 1,
        "is_fake": 0,
        "response": None
    },
    {
        "id": "cb75d13a-f01c-480d-b712-31100f943de4",
        "service_id": "3b3d4e4d-36e4-4436-bea1-63af2117d0bc",
        "name": "healthCheck",
        "url": "/api/project1/health",
        "method": "GET",
        "des": "判断微服务状态是否正常可用",
        "parameter_type": 0,
        "response_type": 0,
        "is_fake": 0,
        "response": None
    },
    {
        "id": "904c2305-27e8-41ef-9ae3-0c26d4271423",
        "service_id": "4fda9469-dcd7-4032-affb-9c9df0cd2cc6",
        "name": "predict",
        "url": "/api/project2/predict",
        "method": "POST",
        "des": "模型推理接口，基于数据集和参数配置得到风险识别结果",
        "parameter_type": 2,
        "response_type": 1,
        "is_fake": 0,
        "response": None
    },
    {
        "id": "e1f56af9-4e78-4e02-b9ac-1e4ca2cdd302",
        "service_id": "4fda9469-dcd7-4032-affb-9c9df0cd2cc6",
        "name": "healthCheck",
        "url": "/api/project2/health",
        "method": "GET",
        "des": "判断微服务状态是否正常可用",
        "parameter_type": 0,
        "response_type": 0,
        "is_fake": 0,
        "response": None
    },
    {
        "id": "bc069861-ab8c-4ecd-879a-5edf16fb8d0c",
        "service_id": "dce40ba0-b5bb-4508-bd09-38a95a2e2932",
        "name": "train",
        "url": "https://myApiServer.com/technical-assessment/train",
        "method": "POST",
        "des": "",
        "parameter_type": 2,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u8bad\\u7ec3\\u5b8c\\u6210!\", \"data\": {\"modelId\": \"2\", \"modelName\": \"model2\", \"modelVersion\": \"1.0\", \"modelPath\": \"/appdata/aml/model/model2.pkl\"}}"
    },
    {
        "id": "b51e6c47-e001-4bd0-91d7-75083e81eb7c",
        "service_id": "dce40ba0-b5bb-4508-bd09-38a95a2e2932",
        "name": "predict",
        "url": "https://myApiServer.com/technical-assessment/predict",
        "method": "POST",
        "des": "",
        "parameter_type": 2,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u9884\\u6d4b\\u6210\\u529f\\uff01\", \"data\": {\"predictResult\": \"predict result list\"}}"
    },
    {
        "id": "12a38525-ac78-4cd4-b774-42f4d494856b",
        "service_id": "01a951d1-09b1-4d65-9f6c-cf048e5f620e",
        "name": "getReportData",
        "url": "https://myApiServer.com/report/get",
        "method": "GET",
        "des": "",
        "parameter_type": 1,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u83b7\\u53d6\\u6210\\u529f!\", \"data\": {\"result\": \"\\u57fa\\u4e8e\\u56fe\\u795e\\u7ecf\\u7f51\\u7edc\\u7684\\u8de8\\u5883\\u8d38\\u6613\\u652f\\u4ed8\\u76d1\\u6d4b\\u6a21\\u578b\\u7684\\u63a8\\u7406\\u7ed3\\u679c\\u5df2\\u7ecf\\u4ea7\\u751f\\u3002\\u6a21\\u578b\\u5728\\u6570\\u636e\\u96c6\\u4e0a\\u7684\\u8868\\u73b0\\u5982\\u4e0b\\uff1a\\n    \\n    \\u5728100\\u4e2a\\u8282\\u70b9\\u4e2d\\uff0c\\u670993\\u4e2a\\u8282\\u70b9\\u88ab\\u5224\\u5b9a\\u4e3a\\u7c7b\\u522b0\\uff0c7\\u4e2a\\u8282\\u70b9\\u88ab\\u5224\\u5b9a\\u4e3a\\u7c7b\\u522b2\\u3002\\u5177\\u4f53\\u7ed3\\u679c\\u5982\\u4e0b\\uff1a\\n    \\n    - \\u7c7b\\u522b0\\uff1a\\u8282\\u70b91\\uff0c\\u8282\\u70b92\\uff0c\\u8282\\u70b93\\uff0c\\u8282\\u70b94\\uff0c\\u8282\\u70b99\\uff0c\\u8282\\u70b910\\uff0c\\u8282\\u70b911\\uff0c\\u8282\\u70b912\\uff0c\\u8282\\u70b913\\uff0c\\u8282\\u70b914\\uff0c\\u8282\\u70b915\\uff0c\\u8282\\u70b916\\uff0c\\u8282\\u70b917\\uff0c\\u8282\\u70b9\\n    18\\uff0c\\u8282\\u70b919\\uff0c\\u8282\\u70b920\\uff0c\\u8282\\u70b921\\uff0c\\u8282\\u70b922\\uff0c\\u8282\\u70b923\\uff0c\\u8282\\u70b924\\uff0c\\u8282\\u70b925\\uff0c\\u8282\\u70b926\\uff0c\\u8282\\u70b927\\uff0c\\u8282\\u70b928\\uff0c\\u8282\\u70b929\\uff0c\\u8282\\u70b930\\uff0c\\u8282\\u70b931\\uff0c\\u8282\\u70b9\\n    32\\uff0c\\u8282\\u70b933\\uff0c\\u8282\\u70b934\\uff0c\\u8282\\u70b935\\uff0c\\u8282\\u70b936\\uff0c\\u8282\\u70b937\\uff0c\\u8282\\u70b938\\uff0c\\u8282\\u70b939\\uff0c\\u8282\\u70b940\\uff0c\\u8282\\u70b941\\uff0c\\u8282\\u70b942\\uff0c\\u8282\\u70b943\\uff0c\\u8282\\u70b944\\uff0c\\u8282\\u70b945\\uff0c\\u8282\\u70b9\\n    46\\uff0c\\u8282\\u70b947\\uff0c\\u8282\\u70b948\\uff0c\\u8282\\u70b949\\uff0c\\u8282\\u70b950\\uff0c\\u8282\\u70b951\\uff0c\\u8282\\u70b952\\uff0c\\u8282\\u70b953\\uff0c\\u8282\\u70b954\\uff0c\\u8282\\u70b955\\uff0c\\u8282\\u70b956\\uff0c\\u8282\\u70b957\\uff0c\\u8282\\u70b958\\uff0c\\u8282\\u70b959\\uff0c\\u8282\\u70b9\\n    60\\uff0c\\u8282\\u70b961\\uff0c\\u8282\\u70b962\\uff0c\\u8282\\u70b963\\uff0c\\u8282\\u70b965\\uff0c\\u8282\\u70b966\\uff0c\\u8282\\u70b967\\uff0c\\u8282\\u70b968\\uff0c\\u8282\\u70b969\\uff0c\\u8282\\u70b970\\uff0c\\u8282\\u70b971\\uff0c\\u8282\\u70b972\\uff0c\\u8282\\u70b973\\uff0c\\u8282\\u70b974\\uff0c\\u8282\\u70b9\\n    75\\uff0c\\u8282\\u70b976\\uff0c\\u8282\\u70b977\\uff0c\\u8282\\u70b978\\uff0c\\u8282\\u70b979\\uff0c\\u8282\\u70b980\\uff0c\\u8282\\u70b981\\uff0c\\u8282\\u70b982\\uff0c\\u8282\\u70b983\\uff0c\\u8282\\u70b984\\uff0c\\u8282\\u70b985\\uff0c\\u8282\\u70b986\\uff0c\\u8282\\u70b987\\uff0c\\u8282\\u70b988\\uff0c\\u8282\\u70b9\\n    89\\uff0c\\u8282\\u70b990\\uff0c\\u8282\\u70b991\\uff0c\\u8282\\u70b992\\uff0c\\u8282\\u70b993\\uff0c\\u8282\\u70b994\\uff0c\\u8282\\u70b995\\uff0c\\u8282\\u70b996\\u3002\\n    \\n    - \\u7c7b\\u522b2\\uff1a\\u8282\\u70b90\\uff0c\\u8282\\u70b95\\uff0c\\u8282\\u70b96\\uff0c\\u8282\\u70b97\\uff0c\\u8282\\u70b98\\uff0c\\u8282\\u70b964\\uff0c\\u8282\\u70b997\\uff0c\\u8282\\u70b998\\uff0c\\u8282\\u70b999\\u3002\\n    \\n    \\u603b\\u7ed3\\uff0c\\u5927\\u591a\\u6570\\u8282\\u70b9\\uff0893%\\uff09\\u88ab\\u5206\\u7c7b\\u4e3a\\u7c7b\\u522b0\\uff0c\\u800c\\u8f83\\u5c0f\\u7684\\u90e8\\u5206\\uff087%\\uff09\\u88ab\\u5206\\u7c7b\\u4e3a\\u7c7b\\u522b2\\u3002\\u8fd9\\u53ef\\u80fd\\u53cd\\u6620\\u4e86\\u5728\\u8bad\\u7ec3\\u96c6\\u4e2d\\u7c7b\\u522b0\\u7684\\u6837\\u672c\\u6570\\u91cf\\u66f4\\u591a\\n    \\uff0c\\u6a21\\u578b\\u5728\\u8bc6\\u522b\\u7c7b\\u522b0\\u7684\\u80fd\\u529b\\u4e0a\\u8868\\u73b0\\u5f97\\u66f4\\u597d\\u3002\\u540c\\u65f6\\uff0c\\u6a21\\u578b\\u5bf9\\u4e8e\\u7c7b\\u522b2\\u7684\\u8bc6\\u522b\\u4e5f\\u6709\\u4e00\\u5b9a\\u7684\\u80fd\\u529b\\u3002\"}}"
    },
    {
        "id": "f954d5f7-6b14-4435-a670-1df8ed84b5b4",
        "service_id": "01a951d1-09b1-4d65-9f6c-cf048e5f620e",
        "name": "sendReport",
        "url": "https://myApiServer.com/report/send",
        "method": "GET",
        "des": "",
        "parameter_type": 1,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u53d1\\u9001\\u6210\\u529f\\uff01\", \"data\": {\"reportId\": \"1\"}}"
    },
    {
        "id": "ef722cf8-7cf6-49e5-9933-c2df97de5336",
        "service_id": "01a951d1-09b1-4d65-9f6c-cf048e5f620e",
        "name": "generateReport",
        "url": "https://myApiServer.com/report-generation/generate",
        "method": "POST",
        "des": "报告生成接口样例",
        "parameter_type": 3,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u751f\\u6210\\u6210\\u529f\\uff01\", \"data\": {\"reportPath\": \"/appdata/aml/report/report1.pdf\"}}"
    },
    {
        "id": "01141636-94fa-46ce-9b73-ee9936e84c6c",
        "service_id": "fde67dc7-39a2-4378-a5fe-ceec617d802f",
        "name": "train",
        "url": "https://myApiServer.com/credit-assessment/train",
        "method": "POST",
        "des": "",
        "parameter_type": 2,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u8bad\\u7ec3\\u5b8c\\u6210!\", \"data\": {\"modelId\": \"4\", \"modelName\": \"model4\", \"modelVersion\": \"1.0\", \"modelPath\": \"/appdata/aml/model/model3.pkl\"}}"
    },
    {
        "id": "40a174ab-9163-4c3a-baa1-5cd561d3e8dc",
        "service_id": "fde67dc7-39a2-4378-a5fe-ceec617d802f",
        "name": "predict",
        "url": "https://myApiServer.com/credit-assessment/predict",
        "method": "POST",
        "des": "",
        "parameter_type": 2,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u9884\\u6d4b\\u6210\\u529f\\uff01\", \"data\": {\"predictResult\": \"predict result list\"}}"
    },
    {
        "id": "241ea618-ca42-42d3-849d-01feea694b0e",
        "service_id": "1f464c6b-6b49-4fa2-8ec9-6942815f7d8f",
        "name": "preprocess",
        "url": "https://myApiServer.com/anomaly-detection/preprocess",
        "method": "POST",
        "des": "",
        "parameter_type": 2,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u9884\\u5904\\u7406\\u6210\\u529f!\", \"data\": {\"modelId\": \"4\", \"modelName\": \"model4\", \"modelVersion\": \"1.0\", \"modelPath\": \"/appdata/aml/data/data4.pkl\"}}"
    },
    {
        "id": "e4564d18-0e2d-4954-b141-afd2bf78a00e",
        "service_id": "1f464c6b-6b49-4fa2-8ec9-6942815f7d8f",
        "name": "train",
        "url": "https://myApiServer.com/anomaly-detection/train",
        "method": "POST",
        "des": "",
        "parameter_type": 2,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u8bad\\u7ec3\\u5b8c\\u6210!\", \"data\": {\"modelId\": \"4\", \"modelName\": \"model4\", \"modelVersion\": \"1.0\", \"modelPath\": \"/appdata/aml/model/model4.pkl\"}}"
    },
    {
        "id": "8cb5c5ec-1ff5-45cd-9b74-b3128f4835c2",
        "service_id": "1f464c6b-6b49-4fa2-8ec9-6942815f7d8f",
        "name": "predict",
        "url": "https://myApiServer.com/anomaly-detection/predict",
        "method": "POST",
        "des": "",
        "parameter_type": 2,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u9884\\u6d4b\\u6210\\u529f\\uff01\", \"data\": {\"predictResult\": \"predict result list\"}}"
    },
    {
        "id": "25baef13-cb6f-479a-a93b-631ba7bbede9",
        "service_id": "1f464c6b-6b49-4fa2-8ec9-6942815f7d8f",
        "name": "evaluate",
        "url": "https://myApiServer.com/anomaly-detection/evaluate",
        "method": "POST",
        "des": "",
        "parameter_type": 2,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u8bc4\\u4f30\\u6210\\u529f\\uff01\", \"data\": {\"evaluateResult\": \"evaluate result list\"}}"
    },
    {
        "id": "0fc3e43d-100a-49ac-b235-78051bcd1164",
        "service_id": "1f464c6b-6b49-4fa2-8ec9-6942815f7d8f",
        "name": "visualize",
        "url": "https://myApiServer.com/anomaly-detection/visualize",
        "method": "POST",
        "des": "",
        "parameter_type": 2,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u53ef\\u89c6\\u5316\\u6210\\u529f\\uff01\", \"data\": {\"visualizeResult\": \"visualize result list\"}}"
    },
    {
        "id": "4ba7146b-2bdc-4b78-bc50-35026f466b8a",
        "service_id": "b352ae47-92db-4281-8faf-9491ab6baea3",
        "name": "generate-report",
        "url": "/api/project3/generate-report",
        "method": "GET",
        "des": "根据自然语言需求生成风险评估报告",
        "parameter_type": 1,
        "response_type": 2,
        "is_fake": 0,
        "response": None
    },
    {
        "id": "6b12525f-90fc-4cda-baf7-11c37d1b1618",
        "service_id": "b352ae47-92db-4281-8faf-9491ab6baea3",
        "name": "nl2gql",
        "url": "/api/project3/nl2gql",
        "method": "GET",
        "des": "根据自然语言需求生成gql语句并得到查询结果",
        "parameter_type": 1,
        "response_type": 1,
        "is_fake": 0,
        "response": None
    },
    {
        "id": "0135556b-757d-4c5f-8347-4eb934549c25",
        "service_id": "b352ae47-92db-4281-8faf-9491ab6baea3",
        "name": "healthCheck",
        "url": "/api/project3/health",
        "method": "GET",
        "des": "判断微服务状态是否正常可用",
        "parameter_type": 0,
        "response_type": 0,
        "is_fake": 0,
        "response": None
    },
    {
        "id": "00c6af38-3aa2-4050-be0c-00c837c8cd42",
        "service_id": "c482ad98-4a7b-4498-a4d5-a52f991d1c0d",
        "name": "safety-fingerprint",
        "url": "/api/project4/safety/safety-fingerprint",
        "method": "POST",
        "des": "",
        "parameter_type": 2,
        "response_type": 1,
        "is_fake": 0,
        "response": None
    },
    {
        "id": "96465be8-ed19-45eb-8920-4980e2d2809f",
        "service_id": "c482ad98-4a7b-4498-a4d5-a52f991d1c0d",
        "name": "healthCheck",
        "url": "/api/project4/safety/health",
        "method": "GET",
        "des": "",
        "parameter_type": 0,
        "response_type": 0,
        "is_fake": 0,
        "response": None
    },
    {
        "id": "92d23e76-b104-4924-8b15-c6588c063255",
        "service_id": "b1b8417a-145c-43e3-b0d1-1aa3d7279c6b",
        "name": "技术评测元应用",
        "url": "https://myApiServer.com/metaApp",
        "method": "POST",
        "des": "",
        "parameter_type": 3,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u8bc4\\u6d4b\\u5b8c\\u6bd5\\uff01\", \"data\": {\"securityResult\": \"5.0\", \"robustnessResult\": \"5.0\", \"privacyResult\": \"5.0\", \"credibilityResult\": \"5.0\"}}"
    },
    {
        "id": "94395fbc-7349-4a06-80db-04c417f4bd04",
        "service_id": "57b897b2-f191-4ede-98d6-46aaee8bd4e8",
        "name": "无人机智能投递",
        "url": "https://myApiServer.com/air/target",
        "method": "POST",
        "des": "",
        "parameter_type": 3,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u4efb\\u52a1\\u5df2\\u5f00\\u59cb\"}"
    },
    {
        "id": "402cb58e-5214-4a5d-b945-16f7c8651307",
        "service_id": "fa3fafbb-fb30-492d-93cf-b608e06b4d99",
        "name": "calculate",
        "url": "/api/linezolid/calculate",
        "method": "POST",
        "des": "根据患者的基本信息计算推荐的利奈唑胺给药剂量",
        "parameter_type": 3,
        "response_type": 1,
        "is_fake": 0,
        "response": None
    },
    {
        "id": "dc107441-be24-4e48-9652-3cd7781e90d3",
        "service_id": "fa3fafbb-fb30-492d-93cf-b608e06b4d99",
        "name": "healthCheck",
        "url": "/api/linezolid/health",
        "method": "GET",
        "des": "判断微服务状态是否正常可用",
        "parameter_type": 0,
        "response_type": 0,
        "is_fake": 0,
        "response": None
    },
    {
        "id": "53c9fa26-03db-4a99-b91f-564c49ed1651",
        "service_id": "f6c3c542-59ed-4277-b771-21f5191d8c5c",
        "name": "diagnose",
        "url": "https://myApiServer.com/health/diagnose",
        "method": "POST",
        "des": "模型推理接口，基于医学影像数据进行辅助诊断",
        "parameter_type": 2,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u8bca\\u65ad\\u5b8c\\u6210\\uff01\", \"data\": {\"diagnosisResult\": \"\\u9ad8\\u5ea6\\u7591\\u4f3c\\u80ba\\u90e8\\u611f\\u67d3\\uff0c\\u5efa\\u8bae\\u8fdb\\u4e00\\u6b65\\u68c0\\u67e5\", \"confidence\": 0.89, \"annotations\": {\"regions\": [{\"x\": 120, \"y\": 150, \"width\": 50, \"height\": 40}, {\"x\": 200, \"y\": 180, \"width\": 30, \"height\": 25}], \"type\": \"\\u5f02\\u5e38\\u533a\\u57df\"}}}"
    },
    {
        "id": "8bd6100c-5dee-4f71-ac84-a2090fc6ca28",
        "service_id": "f6c3c542-59ed-4277-b771-21f5191d8c5c",
        "name": "healthCheck",
        "url": "https://myApiServer.com/health/health",
        "method": "GET",
        "des": "判断微服务状态是否正常可用",
        "parameter_type": 0,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u670d\\u52a1\\u8fd0\\u884c\\u6b63\\u5e38\", \"data\": {\"status\": \"healthy\", \"uptime\": \"72h 15m\"}}"
    },
    {
        "id": "8b00114e-2171-439a-968b-24302b2c036c",
        "service_id": "fd918206-0564-408b-a096-efd3b64c4efc",
        "name": "analyze",
        "url": "https://myApiServer.com/health/monitor/analyze",
        "method": "POST",
        "des": "分析健康数据并提供管理建议",
        "parameter_type": 2,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u5206\\u6790\\u5b8c\\u6210\\uff01\", \"data\": {\"patientStatus\": \"\\u8840\\u7cd6\\u6c34\\u5e73\\u6ce2\\u52a8\\u8f83\\u5927\", \"riskLevel\": \"\\u4e2d\\u7b49\", \"recommendations\": [\"\\u589e\\u52a0\\u9910\\u540e30\\u5206\\u949f\\u6d4b\\u91cf\\u9891\\u7387\", \"\\u8c03\\u6574\\u80f0\\u5c9b\\u7d20\\u7528\\u91cf\", \"\\u6bcf\\u65e530\\u5206\\u949f\\u4f4e\\u5f3a\\u5ea6\\u8fd0\\u52a8\"], \"nextCheckupDate\": \"2023-06-15\"}}"
    },
    {
        "id": "d6e2cc85-ac02-4a79-98c8-b1a3155c14be",
        "service_id": "fd918206-0564-408b-a096-efd3b64c4efc",
        "name": "alert",
        "url": "https://myApiServer.com/health/monitor/alert",
        "method": "POST",
        "des": "设置健康预警阈值和通知",
        "parameter_type": 2,
        "response_type": 0,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u9884\\u8b66\\u8bbe\\u7f6e\\u6210\\u529f\\uff01\", \"data\": {\"alertId\": \"12345\", \"thresholds\": {\"bloodPressureHigh\": \"140/90\", \"bloodPressureLow\": \"90/60\", \"bloodSugarHigh\": \"11.1\", \"bloodSugarLow\": \"3.9\"}, \"notificationChannels\": [\"SMS\", \"App\", \"Family\"]}}"
    },
    {
        "id": "15a001b4-cfa0-4f4e-881a-8374d650f7d7",
        "service_id": "e54ba826-ad95-45aa-928a-cea6d2d94e2a",
        "name": "transcribe",
        "url": "https://myApiServer.com/health/voice/transcribe",
        "method": "POST",
        "des": "将方言语音转写为标准文字",
        "parameter_type": 2,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u8f6c\\u5199\\u6210\\u529f\\uff01\", \"data\": {\"originalDialect\": \"\\u56db\\u5ddd\\u65b9\\u8a00\", \"standardText\": \"\\u6211\\u6700\\u8fd1\\u611f\\u89c9\\u8eab\\u4f53\\u4e0d\\u592a\\u8212\\u670d\\uff0c\\u5934\\u6655\\u5934\\u75db\\uff0c\\u60f3\\u6302\\u53f7\\u770b\\u533b\\u751f\", \"confidence\": 0.92, \"duration\": \"15\\u79d2\", \"medicalTerms\": [{\"term\": \"\\u5934\\u6655\", \"standard\": true}, {\"term\": \"\\u5934\\u75db\", \"standard\": true}]}}"
    },
    {
        "id": "a6c63357-3920-48aa-b0bb-6bff0887270b",
        "service_id": "957f8b36-d0c7-462a-9041-cfb2e063f328",
        "name": "allocate",
        "url": "https://myApiServer.com/health/resource/allocate",
        "method": "POST",
        "des": "根据急诊情况优化医疗资源调度",
        "parameter_type": 2,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u8d44\\u6e90\\u8c03\\u5ea6\\u5b8c\\u6210\\uff01\", \"data\": {\"emergencyLevel\": \"\\u4e2d\\u5ea6\\u7d27\\u6025\", \"allocatedResources\": [{\"type\": \"\\u6551\\u62a4\\u8f66\", \"eta\": \"15\\u5206\\u949f\", \"distance\": \"8.5\\u516c\\u91cc\"}, {\"type\": \"\\u6025\\u8bca\\u533b\\u5e08\", \"status\": \"\\u5f85\\u547d\", \"specialty\": \"\\u5185\\u79d1\"}], \"nearestHospital\": {\"name\": \"\\u53bf\\u4eba\\u6c11\\u533b\\u9662\", \"distance\": \"12\\u516c\\u91cc\", \"availableBeds\": 3, \"specialtyAvailable\": [\"\\u5185\\u79d1\", \"\\u5916\\u79d1\", \"\\u6025\\u8bca\"]}, \"alternativeFacilities\": [{\"name\": \"\\u9547\\u536b\\u751f\\u9662\", \"distance\": \"3\\u516c\\u91cc\", \"capabilities\": \"\\u57fa\\u7840\\u5904\\u7406\"}]}}"
    },
    {
        "id": "b2cfa692-30f9-46eb-bfb4-a5d9524cf286",
        "service_id": "cd670e2a-8567-437d-8dd2-27eee559be19",
        "name": "predict",
        "url": "https://myApiServer.com/health/epidemic/predict",
        "method": "POST",
        "des": "分析历史数据预测流行病发展趋势",
        "parameter_type": 2,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u9884\\u6d4b\\u5206\\u6790\\u5b8c\\u6210\\uff01\", \"data\": {\"diseaseName\": \"\\u5b63\\u8282\\u6027\\u6d41\\u611f\", \"riskLevel\": \"\\u9ad8\", \"predictedPeakTime\": \"2023\\u5e7412\\u6708\\u4e0a\\u65ec\", \"affectedAreas\": [{\"name\": \"\\u6653\\u5e84\\u6751\", \"riskLevel\": \"\\u6781\\u9ad8\", \"population\": 1200}, {\"name\": \"\\u6cb3\\u897f\\u9547\", \"riskLevel\": \"\\u9ad8\", \"population\": 5000}, {\"name\": \"\\u4e1c\\u6797\\u53bf\", \"riskLevel\": \"\\u4e2d\", \"population\": 32000}], \"preventionRecommendations\": [\"\\u63d0\\u524d\\u4e24\\u5468\\u5f00\\u59cb\\u75ab\\u82d7\\u63a5\\u79cd\", \"\\u52a0\\u5f3a\\u5b66\\u6821\\u548c\\u516c\\u5171\\u573a\\u6240\\u6d88\\u6bd2\", \"\\u51c6\\u5907\\u5145\\u8db3\\u533b\\u7597\\u7269\\u8d44\"], \"predictionAccuracy\": \"85%\"}}"
    },
    {
        "id": "7ead28c2-508f-45d6-9f3f-c74bf76240f3",
        "service_id": "fa4c11e8-e76a-49c5-903a-9634dc3abe67",
        "name": "乡村医疗AI辅助诊断元应用",
        "url": "https://myApiServer.com/health/metaApp",
        "method": "POST",
        "des": "",
        "parameter_type": 3,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u8bca\\u65ad\\u5b8c\\u6210\\uff01\", \"data\": {\"patientInfo\": {\"age\": 65, \"gender\": \"\\u7537\", \"symptoms\": [\"\\u80f8\\u95f7\", \"\\u54b3\\u55fd\", \"\\u53d1\\u70ed\"], \"medicalHistory\": \"\\u9ad8\\u8840\\u538b\\uff0c2\\u578b\\u7cd6\\u5c3f\\u75c5\"}, \"diagnosisResult\": {\"primaryDiagnosis\": \"\\u80ba\\u90e8\\u611f\\u67d3\", \"confidence\": 0.92, \"alternativeDiagnosis\": [\"\\u6162\\u6027\\u652f\\u6c14\\u7ba1\\u708e\", \"\\u80ba\\u6c14\\u80bf\"], \"riskLevel\": \"\\u4e2d\\u9ad8\\u98ce\\u9669\"}, \"recommendations\": [\"\\u5efa\\u8bae\\u8fdb\\u884c\\u6297\\u751f\\u7d20\\u6cbb\\u7597\", \"\\u5bc6\\u5207\\u76d1\\u6d4b\\u8840\\u6c27\\u6c34\\u5e73\", \"\\u4e00\\u5468\\u540e\\u590d\\u67e5\"], \"referralNeeded\": true, \"referToSpecialist\": \"\\u547c\\u5438\\u79d1\\u4e13\\u5bb6\"}}"
    },
    {
        "id": "64177ab7-ed48-4e86-913f-f14c6d1fa397",
        "service_id": "80b3b5e1-f2bc-4cd2-a196-0298aa8cc57a",
        "name": "农村公共卫生监测元应用",
        "url": "https://myApiServer.com/health/publicHealth/monitor",
        "method": "POST",
        "des": "",
        "parameter_type": 3,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u5206\\u6790\\u5b8c\\u6210\\uff01\", \"data\": {\"regionOverview\": {\"name\": \"\\u4e1c\\u6797\\u53bf\\u53ca\\u5468\\u8fb9\\u4e61\\u9547\", \"population\": 120000, \"medicalFacilities\": 15, \"healthcareWorkers\": 230}, \"epidemicStatus\": {\"currentOutbreaks\": [{\"disease\": \"\\u5b63\\u8282\\u6027\\u6d41\\u611f\", \"cases\": 325, \"trend\": \"\\u4e0a\\u5347\"}, {\"disease\": \"\\u624b\\u8db3\\u53e3\\u75c5\", \"cases\": 48, \"trend\": \"\\u7a33\\u5b9a\"}], \"predictions\": [{\"disease\": \"\\u5b63\\u8282\\u6027\\u6d41\\u611f\", \"peakTime\": \"2023\\u5e7412\\u6708\\u4e0a\\u65ec\", \"estimatedCases\": 500}, {\"disease\": \"\\u8179\\u6cfb\", \"peakTime\": \"2023\\u5e747\\u6708\", \"estimatedCases\": 200}]}, \"resourceAllocation\": {\"criticalShortages\": [\"\\u513f\\u79d1\\u533b\\u751f\", \"\\u547c\\u5438\\u79d1\\u4e13\\u5bb6\"], \"recommendedDistribution\": [{\"resource\": \"\\u6d41\\u611f\\u75ab\\u82d7\", \"allocateTo\": [\"\\u6cb3\\u897f\\u9547\", \"\\u6653\\u5e84\\u6751\"], \"quantity\": 2000}, {\"resource\": \"\\u9632\\u62a4\\u53e3\\u7f69\", \"allocateTo\": [\"\\u6240\\u6709\\u5b66\\u6821\", \"\\u517b\\u8001\\u9662\"], \"quantity\": 10000}]}, \"preventionActions\": [\"\\u52a0\\u5f3a\\u5b66\\u6821\\u6668\\u68c0\", \"\\u63d0\\u524d\\u542f\\u52a8\\u75ab\\u82d7\\u63a5\\u79cd\\u8ba1\\u5212\", \"\\u519c\\u6751\\u533b\\u751f\\u57f9\\u8bad\"]}}"
    },
    {
        "id": "b278a7e5-d0f6-400f-a565-99f4d68cd1b2",
        "service_id": "4f35b674-4a5b-4b69-a55c-ef0a0ccf2553",
        "name": "analyzeImage",
        "url": "https://myApiServer.com/agriculture/image/analyze",
        "method": "POST",
        "des": "分析农作物图像，识别生长状态",
        "parameter_type": 2,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u5206\\u6790\\u6210\\u529f\", \"data\": {\"status\": \"healthy\", \"growthStage\": \"flowering\", \"confidence\": 0.95, \"estimatedHarvestDate\": \"2023-09-15\", \"recommendations\": [\"\\u9002\\u91cf\\u6d47\\u6c34\", \"\\u589e\\u52a0\\u5149\\u7167\", \"\\u9632\\u6cbb\\u767d\\u7c89\\u75c5\"], \"nutritionStatus\": {\"nitrogen\": \"\\u9002\\u5b9c\", \"phosphorus\": \"\\u504f\\u4f4e\", \"potassium\": \"\\u9002\\u5b9c\"}}}"
    },
    {
        "id": "5515d3fd-c22c-4b9d-92ed-4b3ef8a8816d",
        "service_id": "4f35b674-4a5b-4b69-a55c-ef0a0ccf2553",
        "name": "healthCheck",
        "url": "https://myApiServer.com/agriculture/health",
        "method": "GET",
        "des": "健康检查接口",
        "parameter_type": 0,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u670d\\u52a1\\u6b63\\u5e38\", \"data\": {\"status\": \"running\", \"uptime\": \"65d 12h 37m\", \"version\": \"2.3.5\", \"memoryUsage\": \"45%\", \"cpuUsage\": \"12%\"}}"
    },
    {
        "id": "df6ee593-4d89-4685-8803-b20dd9a196cf",
        "service_id": "f6be78dc-ac2b-485f-93ec-0f7215797d21",
        "name": "identifyDisease",
        "url": "https://myApiServer.com/agriculture/disease/identify",
        "method": "POST",
        "des": "识别农作物病虫害",
        "parameter_type": 2,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u8bc6\\u522b\\u6210\\u529f\", \"data\": {\"disease\": \"\\u7a3b\\u761f\\u75c5\", \"confidence\": 0.92, \"severity\": \"\\u4e2d\\u5ea6\", \"affectedArea\": \"30%\", \"treatment\": [\"\\u55b7\\u6d12\\u6740\\u83cc\\u5242\", \"\\u589e\\u52a0\\u901a\\u98ce\"], \"preventionMeasures\": [\"\\u52a0\\u5f3a\\u7530\\u95f4\\u7ba1\\u7406\", \"\\u9009\\u62e9\\u6297\\u75c5\\u54c1\\u79cd\"], \"spreadRisk\": \"\\u9ad8\", \"economicImpact\": \"\\u4ea7\\u91cf\\u53ef\\u80fd\\u964d\\u4f4e15-20%\"}}"
    },
    {
        "id": "06cbf516-10bb-4772-997b-51506c6c32b2",
        "service_id": "f6be78dc-ac2b-485f-93ec-0f7215797d21",
        "name": "healthCheck",
        "url": "https://myApiServer.com/agriculture/disease/health",
        "method": "GET",
        "des": "健康检查接口",
        "parameter_type": 0,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u670d\\u52a1\\u6b63\\u5e38\", \"data\": {\"status\": \"running\", \"uptime\": \"42d 5h 18m\", \"version\": \"1.8.2\", \"memoryUsage\": \"38%\", \"cpuUsage\": \"5%\"}}"
    },
    {
        "id": "a3d0e878-abc9-4fc6-969a-c878abbf9116",
        "service_id": "c5f36a0f-888f-4900-b970-890b13bc0e86",
        "name": "getIrrigationPlan",
        "url": "https://myApiServer.com/agriculture/irrigation/plan",
        "method": "POST",
        "des": "获取智能灌溉计划",
        "parameter_type": 1,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u704c\\u6e89\\u8ba1\\u5212\\u751f\\u6210\\u6210\\u529f\", \"data\": {\"shouldIrrigate\": true, \"recommendedAmount\": 30, \"unit\": \"\\u7acb\\u65b9\\u7c73/\\u4ea9\", \"timing\": \"\\u4eca\\u65e5\\u508d\\u665a\", \"reason\": \"\\u571f\\u58e4\\u6e7f\\u5ea6\\u4f4e\\u4e8e\\u4f5c\\u7269\\u9700\\u6c42\", \"waterSavings\": \"\\u7ea625%\\uff08\\u4e0e\\u4f20\\u7edf\\u704c\\u6e89\\u76f8\\u6bd4\\uff09\", \"nextAssessment\": \"3\\u5929\\u540e\", \"weatherForecast\": \"\\u672a\\u67653\\u5929\\u65e0\\u6709\\u6548\\u964d\\u6c34\", \"irrigationZones\": [{\"zone\": \"A\", \"priority\": \"\\u9ad8\", \"amount\": 35}, {\"zone\": \"B\", \"priority\": \"\\u4e2d\", \"amount\": 30}, {\"zone\": \"C\", \"priority\": \"\\u4f4e\", \"amount\": 25}]}}"
    },
    {
        "id": "0c1b0f22-69e2-470d-bef0-c41508a85dfe",
        "service_id": "c5f36a0f-888f-4900-b970-890b13bc0e86",
        "name": "healthCheck",
        "url": "https://myApiServer.com/agriculture/irrigation/health",
        "method": "GET",
        "des": "健康检查接口",
        "parameter_type": 0,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u670d\\u52a1\\u6b63\\u5e38\", \"data\": {\"status\": \"running\", \"uptime\": \"28d 9h 42m\", \"version\": \"3.1.0\", \"memoryUsage\": \"32%\", \"cpuUsage\": \"8%\"}}"
    },
    {
        "id": "1bffe8a9-fe3d-4878-847d-9c61f72bad41",
        "service_id": "241009ad-8465-44a8-befb-bfb9c000c2cb",
        "name": "predictYield",
        "url": "https://myApiServer.com/agriculture/yield/predict",
        "method": "POST",
        "des": "预测农作物产量",
        "parameter_type": 2,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u4ea7\\u91cf\\u9884\\u6d4b\\u5b8c\\u6210\", \"data\": {\"predictedYield\": 550, \"unit\": \"\\u516c\\u65a4/\\u4ea9\", \"confidenceInterval\": [520, 580], \"harvestDate\": \"2023-10-05\\u81f32023-10-15\", \"comparisonWithLastYear\": \"+5.2%\", \"factors\": [{\"name\": \"\\u6c14\\u5019\\u6761\\u4ef6\", \"impact\": \"\\u6b63\\u9762\", \"description\": \"\\u4eca\\u5e74\\u964d\\u6c34\\u91cf\\u9002\\u5b9c\"}, {\"name\": \"\\u571f\\u58e4\\u72b6\\u51b5\", \"impact\": \"\\u4e2d\\u6027\", \"description\": \"\\u571f\\u58e4\\u80a5\\u529b\\u9002\\u4e2d\"}, {\"name\": \"\\u75c5\\u866b\\u5bb3\\u98ce\\u9669\", \"impact\": \"\\u8d1f\\u9762\", \"description\": \"\\u7a3b\\u98de\\u8671\\u98ce\\u9669\\u589e\\u52a0\"}], \"recommendations\": [\"\\u4f18\\u5316\\u65bd\\u80a5\\u65b9\\u6848\\u53ef\\u80fd\\u8fdb\\u4e00\\u6b65\\u63d0\\u9ad8\\u4ea7\\u91cf\", \"\\u6ce8\\u610f\\u9632\\u6cbb\\u7a3b\\u98de\\u8671\", \"\\u9002\\u5f53\\u5ef6\\u957f\\u704c\\u6e89\\u5468\\u671f\"]}}"
    },
    {
        "id": "6bbc10b3-fc34-4e44-84d1-aefad16d64b6",
        "service_id": "241009ad-8465-44a8-befb-bfb9c000c2cb",
        "name": "healthCheck",
        "url": "https://myApiServer.com/agriculture/yield/health",
        "method": "GET",
        "des": "健康检查接口",
        "parameter_type": 0,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u670d\\u52a1\\u6b63\\u5e38\", \"data\": {\"status\": \"running\", \"uptime\": \"15d 22h 55m\", \"version\": \"2.0.4\", \"memoryUsage\": \"41%\", \"cpuUsage\": \"7%\"}}"
    },
    {
        "id": "2c54e7c3-a640-456b-a419-1a6c0c33784f",
        "service_id": "9fe9c51a-aa30-44b0-95ff-01827ce3b0bf",
        "name": "智慧农业综合管理元应用",
        "url": "https://myApiServer.com/agriculture/metaApp",
        "method": "POST",
        "des": "",
        "parameter_type": 3,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u5206\\u6790\\u5b8c\\u6210\", \"data\": {\"predictedYield\": 550, \"unit\": \"\\u516c\\u65a4/\\u4ea9\", \"confidenceInterval\": [520, 580], \"harvestDate\": \"2023-10-05\\u81f32023-10-15\", \"comparisonWithLastYear\": \"+5.2%\", \"factors\": [{\"name\": \"\\u6c14\\u5019\\u6761\\u4ef6\", \"impact\": \"\\u6b63\\u9762\", \"description\": \"\\u4eca\\u5e74\\u964d\\u6c34\\u91cf\\u9002\\u5b9c\"}, {\"name\": \"\\u571f\\u58e4\\u72b6\\u51b5\", \"impact\": \"\\u4e2d\\u6027\", \"description\": \"\\u571f\\u58e4\\u80a5\\u529b\\u9002\\u4e2d\"}, {\"name\": \"\\u75c5\\u866b\\u5bb3\\u98ce\\u9669\", \"impact\": \"\\u8d1f\\u9762\", \"description\": \"\\u7a3b\\u98de\\u8671\\u98ce\\u9669\\u589e\\u52a0\"}], \"recommendations\": [\"\\u4f18\\u5316\\u65bd\\u80a5\\u65b9\\u6848\\u53ef\\u80fd\\u8fdb\\u4e00\\u6b65\\u63d0\\u9ad8\\u4ea7\\u91cf\", \"\\u6ce8\\u610f\\u9632\\u6cbb\\u7a3b\\u98de\\u8671\", \"\\u9002\\u5f53\\u5ef6\\u957f\\u704c\\u6e89\\u5468\\u671f\"]}}"
    },
    {
        "id": "43b7bde3-167b-46b6-96cb-24fc889b1130",
        "service_id": "ac7a408b-f01c-4565-b73f-fedc8b01a0e3",
        "name": "pathPlanner",
        "url": "https://myApiServer.com/evtol/path/plan",
        "method": "POST",
        "des": "规划飞行路径，避开障碍物",
        "parameter_type": 3,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u8def\\u5f84\\u89c4\\u5212\\u6210\\u529f\\uff01\", \"data\": {\"pathPoints\": [{\"lat\": 31.2304, \"lng\": 121.4737, \"altitude\": 120}, {\"lat\": 31.2324, \"lng\": 121.4757, \"altitude\": 150}, {\"lat\": 31.2354, \"lng\": 121.4787, \"altitude\": 150}, {\"lat\": 31.2384, \"lng\": 121.4817, \"altitude\": 120}], \"estimatedTime\": \"15\\u5206\\u949f\", \"distance\": \"12.5\\u516c\\u91cc\", \"energyConsumption\": \"30%\", \"weatherRisk\": \"\\u4f4e\", \"noFlyZonesAvoided\": 3}}"
    },
    {
        "id": "f14c260d-01f0-4869-8fbd-115f2cf2573c",
        "service_id": "b10e3b56-9f2d-43ff-a14f-fb89810d3557",
        "name": "environmentPerception",
        "url": "https://myApiServer.com/evtol/perception",
        "method": "POST",
        "des": "感知周围环境，识别障碍物和导航信息",
        "parameter_type": 2,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u73af\\u5883\\u611f\\u77e5\\u5b8c\\u6210\\uff01\", \"data\": {\"detectedObjects\": [{\"type\": \"\\u5efa\\u7b51\\u7269\", \"distance\": 120, \"direction\": \"\\u4e1c\\u5317\", \"height\": 80}, {\"type\": \"\\u7535\\u7ebf\", \"distance\": 50, \"direction\": \"\\u6b63\\u524d\\u65b9\", \"height\": 30}, {\"type\": \"\\u5176\\u4ed6\\u98de\\u884c\\u5668\", \"distance\": 500, \"direction\": \"\\u897f\", \"height\": 150, \"velocity\": {\"speed\": 40, \"heading\": 90}}], \"weatherConditions\": {\"visibility\": \"\\u826f\\u597d\", \"windSpeed\": \"5\\u7c73/\\u79d2\", \"windDirection\": \"\\u897f\\u5317\", \"precipitation\": \"\\u65e0\"}, \"terrainFeatures\": {\"slope\": \"\\u5e73\\u5766\", \"elevation\": \"\\u6d77\\u62d435\\u7c73\", \"surfaceType\": \"\\u57ce\\u5e02\\u5efa\\u7b51\\u533a\"}, \"confidenceScore\": 0.92}}"
    },
    {
        "id": "ee524351-3cee-4f2e-929e-7929599f6388",
        "service_id": "b10e3b56-9f2d-43ff-a14f-fb89810d3557",
        "name": "obstacleDetection",
        "url": "https://myApiServer.com/evtol/obstacle",
        "method": "POST",
        "des": "检测障碍物并提供避险建议",
        "parameter_type": 2,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u969c\\u788d\\u7269\\u68c0\\u6d4b\\u5b8c\\u6210\\uff01\", \"data\": {\"obstaclesDetected\": true, \"obstacleCount\": 3, \"criticalObstacles\": 1, \"emergencyAction\": \"\\u5411\\u53f3\\u504f\\u822a15\\u5ea6\", \"timeToImpact\": \"8.5\\u79d2\"}}"
    },
    {
        "id": "c2fe7095-7724-485b-8787-cfe466151280",
        "service_id": "94c085b9-fc0e-4c5b-830f-e97d7d54ede6",
        "name": "flightController",
        "url": "https://myApiServer.com/evtol/control",
        "method": "POST",
        "des": "控制飞行姿态和动作",
        "parameter_type": 3,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u63a7\\u5236\\u547d\\u4ee4\\u5df2\\u6267\\u884c\\uff01\", \"data\": {\"commandStatus\": \"executed\", \"currentAttitude\": {\"pitch\": 5, \"roll\": 0, \"yaw\": 270}, \"currentAltitude\": 150, \"currentSpeed\": 70, \"flightMode\": \"cruise\", \"stability\": \"\\u4f18\\u79c0\", \"responseTime\": \"0.05\\u79d2\"}}"
    },
    {
        "id": "739c6576-9548-4786-9b1f-ab40b9b77951",
        "service_id": "49e9dd74-e61e-4d21-854d-94fe91d8ddd8",
        "name": "batteryManager",
        "url": "https://myApiServer.com/evtol/battery",
        "method": "POST",
        "des": "管理电池能源使用",
        "parameter_type": 3,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u80fd\\u6e90\\u5206\\u6790\\u5b8c\\u6210\\uff01\", \"data\": {\"currentCharge\": \"72%\", \"estimatedRemaining\": \"38\\u5206\\u949f\", \"rangeRemaining\": \"45\\u516c\\u91cc\", \"dischargeCurve\": [{\"time\": 0, \"charge\": 72}, {\"time\": 10, \"charge\": 65}, {\"time\": 20, \"charge\": 58}, {\"time\": 30, \"charge\": 50}], \"recommendations\": [\"\\u964d\\u4f4e\\u98de\\u884c\\u9ad8\\u5ea6\\u53ef\\u5ef6\\u957f\\u7eed\\u822a\\u65f6\\u95f4\", \"\\u51cf\\u5c11\\u6025\\u52a0\\u901f\\u4ee5\\u4f18\\u5316\\u80fd\\u6e90\\u4f7f\\u7528\"], \"criticalLevel\": false, \"optimalSpeed\": 65}}"
    },
    {
        "id": "89f279f7-7784-4b1a-addb-e2f797ac8c65",
        "service_id": "49e9dd74-e61e-4d21-854d-94fe91d8ddd8",
        "name": "energyOptimizer",
        "url": "https://myApiServer.com/evtol/energy/optimize",
        "method": "POST",
        "des": "优化能源使用策略",
        "parameter_type": 3,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u80fd\\u6e90\\u4f18\\u5316\\u5b8c\\u6210\\uff01\", \"data\": {\"optimizedProfile\": {\"climbRate\": \"3\\u7c73/\\u79d2\", \"cruiseSpeed\": \"65\\u516c\\u91cc/\\u5c0f\\u65f6\", \"descentRate\": \"2\\u7c73/\\u79d2\"}, \"energySavings\": \"12%\", \"extendedRange\": \"8\\u516c\\u91cc\", \"batteryHealthImpact\": \"\\u79ef\\u6781\", \"implementationDifficulty\": \"\\u4f4e\"}}"
    },
    {
        "id": "efc07658-7261-4ede-80ee-381788467468",
        "service_id": "46b8c837-2450-4b87-9b41-d91242f51803",
        "name": "safetyMonitor",
        "url": "https://myApiServer.com/evtol/safety",
        "method": "POST",
        "des": "监控飞行安全状态",
        "parameter_type": 3,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u5b89\\u5168\\u72b6\\u6001\\u8bc4\\u4f30\\u5b8c\\u6210\\uff01\", \"data\": {\"overallStatus\": \"\\u6b63\\u5e38\", \"safetyScore\": 95, \"anomalies\": [{\"component\": \"\\u5de6\\u4fa7\\u87ba\\u65cb\\u6868\", \"severity\": \"\\u4f4e\", \"action\": \"\\u7ee7\\u7eed\\u76d1\\u63a7\"}], \"systemChecks\": {\"propulsion\": \"Pass\", \"navigation\": \"Pass\", \"communication\": \"Pass\", \"powertrain\": \"Pass\"}, \"redundancyStatus\": {\"primary\": \"\\u6b63\\u5e38\", \"secondary\": \"\\u51c6\\u5907\\u5c31\\u7eea\"}, \"recommendedActions\": []}}"
    },
    {
        "id": "f9b14d94-1b6e-4aca-9ec7-8fb27ffa054b",
        "service_id": "264342fa-649d-47f9-b589-41f0c592ea14",
        "name": "eVTOL智能飞行控制元应用",
        "url": "https://myApiServer.com/evtol/metaApp",
        "method": "POST",
        "des": "",
        "parameter_type": 3,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u4efb\\u52a1\\u6267\\u884c\\u5b8c\\u6210\\uff01\", \"data\": {\"missionStatus\": \"\\u5b8c\\u6210\", \"flightPath\": [{\"lat\": 31.2304, \"lng\": 121.4737, \"alt\": 120, \"time\": \"14:30:00\"}, {\"lat\": 31.2324, \"lng\": 121.4757, \"alt\": 150, \"time\": \"14:35:00\"}, {\"lat\": 31.2354, \"lng\": 121.4787, \"alt\": 150, \"time\": \"14:40:00\"}, {\"lat\": 31.2384, \"lng\": 121.4817, \"alt\": 120, \"time\": \"14:45:00\"}], \"batteryUsed\": \"28%\", \"obstaclesAvoided\": 5, \"weatherConditions\": \"\\u826f\\u597d\", \"totalFlightTime\": \"15\\u5206\\u949f\", \"safetyIncidents\": 0, \"recommendations\": [\"\\u5b9a\\u671f\\u68c0\\u67e5\\u5de6\\u4fa7\\u87ba\\u65cb\\u6868\", \"\\u66f4\\u65b0\\u57ce\\u533a\\u9ad8\\u5c42\\u5efa\\u7b51\\u6570\\u636e\"]}}"
    },
    {
        "id": "5f5a8758-f2f2-4efa-a54b-585177f3a3b6",
        "service_id": "334d0e8d-dcfe-4f7f-a41e-eb3989147a2a",
        "name": "translateContent",
        "url": "https://myApiServer.com/ecommerce/translate",
        "method": "POST",
        "des": "将产品描述翻译成多种语言",
        "parameter_type": 2,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u7ffb\\u8bd1\\u6210\\u529f\\uff01\", \"data\": {\"translations\": {\"en\": \"Product description in English\", \"es\": \"Descripci\\u00f3n del producto en espa\\u00f1ol\", \"fr\": \"Description du produit en fran\\u00e7ais\"}}}"
    },
    {
        "id": "1ca5b3fc-4063-4bbf-ad3a-07e1a667b2b8",
        "service_id": "334d0e8d-dcfe-4f7f-a41e-eb3989147a2a",
        "name": "generateDescription",
        "url": "https://myApiServer.com/ecommerce/generate",
        "method": "POST",
        "des": "根据产品特性生成营销文案",
        "parameter_type": 2,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u751f\\u6210\\u6210\\u529f\\uff01\", \"data\": {\"marketingText\": \"Generated marketing content based on product features\"}}"
    },
    {
        "id": "7f8dcbe8-1ffd-4553-92ef-abd030b55b86",
        "service_id": "9bd7eb41-81a0-48bf-bfdb-b7f6e7eb33d5",
        "name": "analyzeTrend",
        "url": "https://myApiServer.com/ecommerce/analyze",
        "method": "POST",
        "des": "分析市场趋势及竞品情况",
        "parameter_type": 2,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u5206\\u6790\\u5b8c\\u6210\\uff01\", \"data\": {\"trends\": [\"\\u5317\\u7f8e\\u533a\\u57df\\u9500\\u91cf\\u589e\\u957f15%\", \"\\u6b27\\u6d32\\u5e02\\u573a\\u7ade\\u4e89\\u52a0\\u5267\"], \"recommendations\": [\"\\u589e\\u52a0\\u5e7f\\u544a\\u6295\\u653e\", \"\\u8c03\\u6574\\u5b9a\\u4ef7\\u7b56\\u7565\"]}}"
    },
    {
        "id": "eca2ba57-95d6-4c94-af9c-c156f40882ee",
        "service_id": "9bd7eb41-81a0-48bf-bfdb-b7f6e7eb33d5",
        "name": "predictSales",
        "url": "https://myApiServer.com/ecommerce/predict",
        "method": "POST",
        "des": "预测产品销量及趋势",
        "parameter_type": 2,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u9884\\u6d4b\\u5b8c\\u6210\\uff01\", \"data\": {\"predictedSales\": [125, 142, 156, 168, 172], \"trend\": \"\\u4e0a\\u5347\", \"confidence\": 0.85}}"
    },
    {
        "id": "bfe2c424-8df7-42bf-9cfd-e4b751a116d5",
        "service_id": "0969a474-c3b2-4ddf-99e9-61c3ec4fb076",
        "name": "跨境电商智能营销元应用",
        "url": "https://myApiServer.com/ecommerce/metaApp",
        "method": "POST",
        "des": "执行跨境电商全渠道营销活动",
        "parameter_type": 3,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"code\": 200, \"message\": \"\\u8425\\u9500\\u8ba1\\u5212\\u751f\\u6210\\u6210\\u529f\\uff01\", \"data\": {\"marketingPlan\": {\"channels\": [\"social\", \"email\", \"search\"], \"schedule\": {\"startDate\": \"2023-07-01\", \"endDate\": \"2023-07-31\"}, \"budget\": {\"total\": 5000, \"allocation\": {\"social\": 2500, \"email\": 1000, \"search\": 1500}}}}}"
    },
    {
        "id": "01a6a1bf-4a6d-4bfd-85c1-e00dde8ddc80",
        "service_id": "5290d2a8-777d-4cfa-8ddb-39568bcc25f3",
        "name": "objectDetection",
        "url": "",
        "method": "GET",
        "des": "",
        "parameter_type": 0,
        "response_type": 0,
        "is_fake": 0,
        "response": "{\"name\": \"detectedObjects\", \"description\": \"\\u68c0\\u6d4b\\u5230\\u7684\\u7269\\u4f53\\u5217\\u8868\", \"type\": \"array\"}"
    },
    {
        "id": "33252104-2887-463d-9fc9-aaa10ff5982d",
        "service_id": "5290d2a8-777d-4cfa-8ddb-39568bcc25f3",
        "name": "spatialMapping",
        "url": "",
        "method": "GET",
        "des": "",
        "parameter_type": 0,
        "response_type": 0,
        "is_fake": 0,
        "response": "{\"name\": \"spatialMap\", \"description\": \"3D\\u7a7a\\u95f4\\u5730\\u56fe\", \"type\": \"object\"}"
    },
    {
        "id": "de632961-6f54-4f1b-91a1-0e33990b9930",
        "service_id": "57260e5e-66d0-4d56-8281-a28ee3d550ab",
        "name": "naturalLanguageUnderstanding",
        "url": "",
        "method": "GET",
        "des": "",
        "parameter_type": 0,
        "response_type": 0,
        "is_fake": 0,
        "response": "{\"name\": \"understanding\", \"description\": \"\\u7406\\u89e3\\u7ed3\\u679c\", \"type\": \"object\"}"
    },
    {
        "id": "c7e7459e-25fc-4bff-96fb-0f450d467c80",
        "service_id": "57260e5e-66d0-4d56-8281-a28ee3d550ab",
        "name": "emotionRecognition",
        "url": "",
        "method": "GET",
        "des": "",
        "parameter_type": 0,
        "response_type": 0,
        "is_fake": 0,
        "response": "{\"name\": \"emotionState\", \"description\": \"\\u60c5\\u7eea\\u72b6\\u6001\\u5206\\u6790\", \"type\": \"object\"}"
    },
    {
        "id": "5e3baa59-f572-4dde-9a84-0d31208a571e",
        "service_id": "88a6773d-7274-4071-87df-d4763855f899",
        "name": "vitalSignsMonitor",
        "url": "",
        "method": "GET",
        "des": "",
        "parameter_type": 0,
        "response_type": 0,
        "is_fake": 0,
        "response": "{\"name\": \"vitalSigns\", \"description\": \"\\u751f\\u547d\\u4f53\\u5f81\\u5206\\u6790\\u7ed3\\u679c\", \"type\": \"object\"}"
    },
    {
        "id": "4320d33d-5da0-4ec5-a08f-63e94c9e6ec2",
        "service_id": "88a6773d-7274-4071-87df-d4763855f899",
        "name": "abnormalBehaviorDetection",
        "url": "",
        "method": "GET",
        "des": "",
        "parameter_type": 0,
        "response_type": 0,
        "is_fake": 0,
        "response": "{\"name\": \"anomalyReport\", \"description\": \"\\u5f02\\u5e38\\u884c\\u4e3a\\u62a5\\u544a\", \"type\": \"object\"}"
    },
    {
        "id": "a4f448ad-bfe4-4bd0-957d-84784393a854",
        "service_id": "845f73ed-f998-4e3b-b3f1-74dbdb93a34e",
        "name": "taskPlanner",
        "url": "",
        "method": "GET",
        "des": "",
        "parameter_type": 0,
        "response_type": 0,
        "is_fake": 0,
        "response": "{\"name\": \"taskPlan\", \"description\": \"\\u4efb\\u52a1\\u6267\\u884c\\u8ba1\\u5212\", \"type\": \"object\"}"
    },
    {
        "id": "b620d01c-daf1-4840-ba69-f2505147b017",
        "service_id": "845f73ed-f998-4e3b-b3f1-74dbdb93a34e",
        "name": "pathPlanning",
        "url": "",
        "method": "GET",
        "des": "",
        "parameter_type": 0,
        "response_type": 0,
        "is_fake": 0,
        "response": "{\"name\": \"path\", \"description\": \"\\u89c4\\u5212\\u8def\\u5f84\", \"type\": \"array\"}"
    },
    {
        "id": "e4141f97-f036-484d-95e5-f58738d76011",
        "service_id": "0247718c-34c6-46b7-9a75-abd4b8e615af",
        "name": "家庭智能助手元应用",
        "url": "https://myApiServer.com/evtol/metaApp",
        "method": "POST",
        "des": "",
        "parameter_type": 3,
        "response_type": 1,
        "is_fake": 1,
        "response": "{\"name\": \"assistantResponse\", \"description\": \"\\u52a9\\u624b\\u6267\\u884c\\u7ed3\\u679c\", \"type\": \"object\"}"
    },
]

# MOCK_SERVICE_API_PARAMETERS 数据
MOCK_SERVICE_API_PARAMETERS = [
    {
        "id": "e9a3518d-adac-4579-a4fc-67b42aba6eb8",
        "api_id": "1bfa846d-6fbd-4c1f-a3c9-0b476b03004e",
        "name": "file",
        "type": "zip file",
        "des": "数据集和参数配置文件的zip压缩包"
    },
    {
        "id": "bedb033d-0a09-4034-96b6-f120f4dd46ac",
        "api_id": "904c2305-27e8-41ef-9ae3-0c26d4271423",
        "name": "file",
        "type": "zip file",
        "des": "数据集和参数配置文件的zip压缩包"
    },
    {
        "id": "86f941f5-a357-490c-aecf-3a3e8b571a87",
        "api_id": "12a38525-ac78-4cd4-b774-42f4d494856b",
        "name": "reportId",
        "type": "int",
        "des": ""
    },
    {
        "id": "5c841485-9895-4f49-bf87-6e92936b53d1",
        "api_id": "f954d5f7-6b14-4435-a670-1df8ed84b5b4",
        "name": "reportId",
        "type": "int",
        "des": ""
    },
    {
        "id": "e082f3b3-0e85-46da-93b9-4ab2e3340853",
        "api_id": "ef722cf8-7cf6-49e5-9933-c2df97de5336",
        "name": "reportData",
        "type": "string",
        "des": "用于生成报告的数据"
    },
    {
        "id": "c5cfc860-72f7-4489-a23c-ea74127ac81f",
        "api_id": "4ba7146b-2bdc-4b78-bc50-35026f466b8a",
        "name": "query",
        "type": "string",
        "des": "用自然语言描述想要生成的报告"
    },
    {
        "id": "1cf72f85-5ac0-4cf3-ae7f-990df1de4edb",
        "api_id": "6b12525f-90fc-4cda-baf7-11c37d1b1618",
        "name": "query",
        "type": "string",
        "des": "用自然语言描述查询需求"
    },
    {
        "id": "e2e29273-3868-4cbc-b52a-64ccffe39675",
        "api_id": "00c6af38-3aa2-4050-be0c-00c837c8cd42",
        "name": "file",
        "type": "file",
        "des": "数据集和配置文件的zip压缩包"
    },
    {
        "id": "7fe23425-7b7f-4e3d-9182-1e56006653a0",
        "api_id": "00c6af38-3aa2-4050-be0c-00c837c8cd42",
        "name": "model_name",
        "type": "string",
        "des": "模型名称，目前只支持HattenGCN"
    },
    {
        "id": "d812e73d-2dc0-4208-b19b-4e8aab915dc3",
        "api_id": "402cb58e-5214-4a5d-b945-16f7c8651307",
        "name": "sex",
        "type": "int",
        "des": "性别，0表示女性，1表示男性"
    },
    {
        "id": "43871c18-56f3-4093-95a5-106035e4eb10",
        "api_id": "402cb58e-5214-4a5d-b945-16f7c8651307",
        "name": "age",
        "type": "int",
        "des": "年龄，必须为整数"
    },
    {
        "id": "ed9ecbec-bf5b-4832-b7b8-2d851238e9c8",
        "api_id": "402cb58e-5214-4a5d-b945-16f7c8651307",
        "name": "height",
        "type": "int",
        "des": "身高，单位cm，必须为整数"
    },
    {
        "id": "2b5fadf9-edaf-48f8-83b6-a308417038ea",
        "api_id": "402cb58e-5214-4a5d-b945-16f7c8651307",
        "name": "weight",
        "type": "int",
        "des": "体重，单位kg，必须为整数"
    },
    {
        "id": "1aa1aa98-ac63-4e61-9838-976186bd8fec",
        "api_id": "402cb58e-5214-4a5d-b945-16f7c8651307",
        "name": "scr",
        "type": "float",
        "des": "血清肌酐，单位umol/L，必须为浮点数"
    },
    {
        "id": "0b429d45-c6bd-4045-8984-61a9df18b07d",
        "api_id": "402cb58e-5214-4a5d-b945-16f7c8651307",
        "name": "tb",
        "type": "float",
        "des": "总胆红素，单位umol/L，必须为浮点数"
    },
    {
        "id": "55774d16-5aa1-4806-a143-c29134fb8959",
        "api_id": "402cb58e-5214-4a5d-b945-16f7c8651307",
        "name": "auc_range",
        "type": "array",
        "des": "目标24小时药时曲线AUC范围，单位umol/L，必须为数组，数组长度为2，第一个元素为下限，第二个元素为上限"
    },
    {
        "id": "478ab32a-9ecd-4510-9188-37c7925c1fba",
        "api_id": "53c9fa26-03db-4a99-b91f-564c49ed1651",
        "name": "file",
        "type": "image file",
        "des": "医学影像文件（支持CT、X光、超声等图像）"
    },
    {
        "id": "f19cbf35-62a9-4738-b906-a1fdf0115391",
        "api_id": "8b00114e-2171-439a-968b-24302b2c036c",
        "name": "data",
        "type": "json",
        "des": "来自可穿戴设备和家用医疗设备的健康数据"
    },
    {
        "id": "3f89cd9a-fac9-47d4-b51f-f490f8679336",
        "api_id": "15a001b4-cfa0-4f4e-881a-8374d650f7d7",
        "name": "audio",
        "type": "audio file",
        "des": "语音文件（支持方言）"
    },
    {
        "id": "1b74d9eb-4a4f-4081-9636-4e947d5a901f",
        "api_id": "a6c63357-3920-48aa-b0bb-6bff0887270b",
        "name": "data",
        "type": "json",
        "des": "急诊信息和可用资源数据"
    },
    {
        "id": "46b99ddb-031e-4b42-afc2-049d6fbdf57a",
        "api_id": "b2cfa692-30f9-46eb-bfb4-a5d9524cf286",
        "name": "data",
        "type": "json",
        "des": "历史疫情数据和环境因素"
    },
    {
        "id": "fb2e672f-054c-4c18-857f-5e1191ff7d35",
        "api_id": "b278a7e5-d0f6-400f-a565-99f4d68cd1b2",
        "name": "image",
        "type": "file",
        "des": "农作物图像文件"
    },
    {
        "id": "3820b967-3224-4119-8024-684ee63be414",
        "api_id": "b278a7e5-d0f6-400f-a565-99f4d68cd1b2",
        "name": "cropType",
        "type": "string",
        "des": "作物类型，如不提供则自动识别"
    },
    {
        "id": "ab5416ac-e0a7-48d7-8a0d-5f4f4cd2509f",
        "api_id": "df6ee593-4d89-4685-8803-b20dd9a196cf",
        "name": "image",
        "type": "file",
        "des": "病害部位图像"
    },
    {
        "id": "18f0d7f0-3ea0-482a-90eb-42c4131da936",
        "api_id": "df6ee593-4d89-4685-8803-b20dd9a196cf",
        "name": "cropType",
        "type": "string",
        "des": "作物类型"
    },
    {
        "id": "70bb3420-8822-45cf-ab33-8d3371b687b6",
        "api_id": "a3d0e878-abc9-4fc6-969a-c878abbf9116",
        "name": "soilMoisture",
        "type": "number",
        "des": "土壤湿度百分比"
    },
    {
        "id": "8519c830-ac12-4419-a3df-45520bc4e1e1",
        "api_id": "a3d0e878-abc9-4fc6-969a-c878abbf9116",
        "name": "cropType",
        "type": "string",
        "des": "作物类型"
    },
    {
        "id": "fe32a06c-0449-4d99-9c1b-dbc1272087ff",
        "api_id": "a3d0e878-abc9-4fc6-969a-c878abbf9116",
        "name": "growthStage",
        "type": "string",
        "des": "生长阶段"
    },
    {
        "id": "57288725-c362-4e08-8a04-5cfba076d00d",
        "api_id": "a3d0e878-abc9-4fc6-969a-c878abbf9116",
        "name": "fieldSize",
        "type": "number",
        "des": "田地面积(亩)"
    },
    {
        "id": "fd74ab8a-8d87-4575-80b7-391fa8f3b37d",
        "api_id": "1bffe8a9-fe3d-4878-847d-9c61f72bad41",
        "name": "cropType",
        "type": "string",
        "des": "作物类型"
    },
    {
        "id": "366e00de-a7d9-4c93-9fa3-5072bb63e7df",
        "api_id": "1bffe8a9-fe3d-4878-847d-9c61f72bad41",
        "name": "plantingDate",
        "type": "string",
        "des": "播种日期(YYYY-MM-DD)"
    },
    {
        "id": "ab4f8dba-9800-49d0-9b40-5f3dc12d2c62",
        "api_id": "1bffe8a9-fe3d-4878-847d-9c61f72bad41",
        "name": "fieldSize",
        "type": "number",
        "des": "田地面积(亩)"
    },
    {
        "id": "614cbaa4-dac7-4fb5-9da4-b5cda624d67a",
        "api_id": "1bffe8a9-fe3d-4878-847d-9c61f72bad41",
        "name": "historicalData",
        "type": "file",
        "des": "历史产量数据(CSV)"
    },
    {
        "id": "11775f78-1508-44d6-825d-fec391c7d0ab",
        "api_id": "43b7bde3-167b-46b6-96cb-24fc889b1130",
        "name": "data",
        "type": "json",
        "des": "包含起点终点和环境数据的JSON"
    },
    {
        "id": "9367554c-a25c-47d1-bb29-0fb84e40e5b0",
        "api_id": "f14c260d-01f0-4869-8fbd-115f2cf2573c",
        "name": "sensorData",
        "type": "multimodal",
        "des": "来自多种传感器的数据"
    },
    {
        "id": "93e1ed97-7831-4507-8157-eddbedfc2d41",
        "api_id": "c2fe7095-7724-485b-8787-cfe466151280",
        "name": "controlCommand",
        "type": "json",
        "des": "飞行控制命令"
    },
    {
        "id": "2e0d4642-057d-4fc3-b189-605e368130b3",
        "api_id": "739c6576-9548-4786-9b1f-ab40b9b77951",
        "name": "flightData",
        "type": "json",
        "des": "飞行数据和电池状态"
    },
    {
        "id": "6d91c3a3-29ea-4271-b8e1-017caedc0d90",
        "api_id": "efc07658-7261-4ede-80ee-381788467468",
        "name": "systemStatus",
        "type": "json",
        "des": "系统状态数据"
    },
    {
        "id": "aaf65c88-11ef-40b0-a14e-b81e165eb8b0",
        "api_id": "5f5a8758-f2f2-4efa-a54b-585177f3a3b6",
        "name": "productData",
        "type": "object",
        "des": "产品详细信息"
    },
    {
        "id": "cf342bea-0ebe-4c53-8676-36bd0ecd8e9c",
        "api_id": "5f5a8758-f2f2-4efa-a54b-585177f3a3b6",
        "name": "targetLanguages",
        "type": "array",
        "des": "目标语言列表"
    },
    {
        "id": "b9742a61-f724-4679-9f43-485ea9b8a76d",
        "api_id": "1ca5b3fc-4063-4bbf-ad3a-07e1a667b2b8",
        "name": "productFeatures",
        "type": "array",
        "des": "产品特性列表"
    },
    {
        "id": "d3db2d17-e1dd-4a63-ad37-5818d67c6566",
        "api_id": "1ca5b3fc-4063-4bbf-ad3a-07e1a667b2b8",
        "name": "targetMarket",
        "type": "string",
        "des": "目标市场"
    },
    {
        "id": "56f2bf76-4921-4231-ad99-fdb51200680d",
        "api_id": "1ca5b3fc-4063-4bbf-ad3a-07e1a667b2b8",
        "name": "tone",
        "type": "string",
        "des": "文案风格"
    },
    {
        "id": "6459586d-f088-413a-8161-06b5232faa43",
        "api_id": "7f8dcbe8-1ffd-4553-92ef-abd030b55b86",
        "name": "productCategory",
        "type": "string",
        "des": "产品类别"
    },
    {
        "id": "b4169594-5183-4405-9d7f-deb5b75f7b9d",
        "api_id": "7f8dcbe8-1ffd-4553-92ef-abd030b55b86",
        "name": "targetMarkets",
        "type": "array",
        "des": "目标市场列表"
    },
    {
        "id": "16e2ac40-9759-46c2-9634-4a25db4b7983",
        "api_id": "7f8dcbe8-1ffd-4553-92ef-abd030b55b86",
        "name": "timeRange",
        "type": "object",
        "des": "分析时间范围"
    },
    {
        "id": "7f522c43-8e82-466a-a645-7c6674ad6039",
        "api_id": "eca2ba57-95d6-4c94-af9c-c156f40882ee",
        "name": "productId",
        "type": "string",
        "des": "产品ID"
    },
    {
        "id": "7c63e81e-06d4-4396-b410-ee3197b2db6e",
        "api_id": "eca2ba57-95d6-4c94-af9c-c156f40882ee",
        "name": "historicalData",
        "type": "array",
        "des": "历史销售数据"
    },
    {
        "id": "757c51b2-7933-481e-abc3-253a83910c8c",
        "api_id": "eca2ba57-95d6-4c94-af9c-c156f40882ee",
        "name": "predictionPeriod",
        "type": "number",
        "des": "预测周期（天）"
    },
    {
        "id": "316fc983-0e3c-4c3d-be2e-c265760b8e44",
        "api_id": "bfe2c424-8df7-42bf-9cfd-e4b751a116d5",
        "name": "campaignDetails",
        "type": "object",
        "des": "营销活动详情"
    },
    {
        "id": "1af31374-8bd8-4009-81d4-5ba436e73370",
        "api_id": "bfe2c424-8df7-42bf-9cfd-e4b751a116d5",
        "name": "productData",
        "type": "object",
        "des": "产品数据"
    },
    {
        "id": "4a7cb8f8-2e7b-48bc-8129-9ea3294538e7",
        "api_id": "bfe2c424-8df7-42bf-9cfd-e4b751a116d5",
        "name": "targetMarkets",
        "type": "array",
        "des": "目标市场列表"
    },
    {
        "id": "3897e0ca-fc3d-4a59-b29b-857293ac749f",
        "api_id": "bfe2c424-8df7-42bf-9cfd-e4b751a116d5",
        "name": "budget",
        "type": "object",
        "des": "预算配置"
    },
    {
        "id": "b5868531-4abc-4b54-bf98-9e609e906f37",
        "api_id": "01a6a1bf-4a6d-4bfd-85c1-e00dde8ddc80",
        "name": "imageData",
        "type": "object",
        "des": ""
    },
    {
        "id": "c2175ba5-f06c-4072-ad55-bb8057e353f1",
        "api_id": "01a6a1bf-4a6d-4bfd-85c1-e00dde8ddc80",
        "name": "detectionThreshold",
        "type": "number",
        "des": ""
    },
    {
        "id": "8e31a2f1-abb2-43e4-a2a8-8b433205ae10",
        "api_id": "33252104-2887-463d-9fc9-aaa10ff5982d",
        "name": "depthData",
        "type": "array",
        "des": ""
    },
    {
        "id": "97ecbe4b-31ff-47fd-94ba-1a559a3e333b",
        "api_id": "33252104-2887-463d-9fc9-aaa10ff5982d",
        "name": "resolution",
        "type": "number",
        "des": ""
    },
    {
        "id": "fb4dcb01-5892-4f08-b41b-be50e90ef546",
        "api_id": "de632961-6f54-4f1b-91a1-0e33990b9930",
        "name": "text",
        "type": "string",
        "des": ""
    },
    {
        "id": "2d73d49d-552d-441f-a265-d8ea822435c3",
        "api_id": "de632961-6f54-4f1b-91a1-0e33990b9930",
        "name": "context",
        "type": "object",
        "des": ""
    },
    {
        "id": "d94af69d-7c2e-4226-ae9e-205295b270a0",
        "api_id": "c7e7459e-25fc-4bff-96fb-0f450d467c80",
        "name": "audioData",
        "type": "binary",
        "des": ""
    },
    {
        "id": "24b46d11-b8f4-493e-8ec5-22abce187c4a",
        "api_id": "c7e7459e-25fc-4bff-96fb-0f450d467c80",
        "name": "facialImage",
        "type": "binary",
        "des": ""
    },
    {
        "id": "3231a34f-b93d-4b3c-9406-707b0bab4a55",
        "api_id": "5e3baa59-f572-4dde-9a84-0d31208a571e",
        "name": "sensorData",
        "type": "object",
        "des": ""
    },
    {
        "id": "b91cc68c-8e76-4157-a6be-f7d059be5023",
        "api_id": "5e3baa59-f572-4dde-9a84-0d31208a571e",
        "name": "userProfile",
        "type": "object",
        "des": ""
    },
    {
        "id": "3e0f8073-e709-4029-884c-acd214355077",
        "api_id": "4320d33d-5da0-4ec5-a08f-63e94c9e6ec2",
        "name": "behaviorData",
        "type": "array",
        "des": ""
    },
    {
        "id": "9653d39b-af6a-4b30-8232-9631be9051ec",
        "api_id": "4320d33d-5da0-4ec5-a08f-63e94c9e6ec2",
        "name": "baseline",
        "type": "object",
        "des": ""
    },
    {
        "id": "3e3b8a34-a7f5-4c9e-94d0-541f03d7d574",
        "api_id": "a4f448ad-bfe4-4bd0-957d-84784393a854",
        "name": "taskList",
        "type": "array",
        "des": ""
    },
    {
        "id": "5f4687f6-8e15-452a-b5fe-b8b0f8a94915",
        "api_id": "a4f448ad-bfe4-4bd0-957d-84784393a854",
        "name": "environmentState",
        "type": "object",
        "des": ""
    },
    {
        "id": "02269074-3991-4a0a-aa8c-8ae1150400ae",
        "api_id": "a4f448ad-bfe4-4bd0-957d-84784393a854",
        "name": "preferences",
        "type": "object",
        "des": ""
    },
    {
        "id": "a7f948db-1309-45c4-888d-5358622cab21",
        "api_id": "b620d01c-daf1-4840-ba69-f2505147b017",
        "name": "spatialMap",
        "type": "object",
        "des": ""
    },
    {
        "id": "4fa3e32b-475b-47ec-9b2f-ed290f826149",
        "api_id": "b620d01c-daf1-4840-ba69-f2505147b017",
        "name": "startPosition",
        "type": "object",
        "des": ""
    },
    {
        "id": "b7a72ab5-fc45-445c-b765-5d815cf8b9dd",
        "api_id": "b620d01c-daf1-4840-ba69-f2505147b017",
        "name": "targetPosition",
        "type": "object",
        "des": ""
    },
    {
        "id": "f4df4c1d-068b-4020-bb0b-37304aae9d90",
        "api_id": "e4141f97-f036-484d-95e5-f58738d76011",
        "name": "command",
        "type": "string",
        "des": ""
    },
    {
        "id": "d26f92c6-b501-4164-8c5a-a54d8bc9f537",
        "api_id": "e4141f97-f036-484d-95e5-f58738d76011",
        "name": "environmentData",
        "type": "object",
        "des": ""
    },
    {
        "id": "d120adb2-0a54-4412-bf00-9a4488c4daa1",
        "api_id": "e4141f97-f036-484d-95e5-f58738d76011",
        "name": "userContext",
        "type": "object",
        "des": ""
    },
    {
        "id": "adb61a4a-9791-4eae-93c5-46e87d3f1206",
        "api_id": "e4141f97-f036-484d-95e5-f58738d76011",
        "name": "executionMode",
        "type": "string",
        "des": ""
    },
]
