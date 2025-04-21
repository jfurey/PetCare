-- Vaccinations for Max (Dog - Golden Retriever)
INSERT INTO vaccinations (pet_id, veterinarian_id, veterinarian_name, vaccine_name, date_given, next_due, created_at) VALUES
(1, 1, 'Dr. Sarah Williams', 'Rabies', '2023-01-15', '2024-01-15', NOW()),
(1, 1, 'Dr. Sarah Williams', 'DHPP', '2023-02-10', '2024-02-10', NOW()),
(1, 4, 'Dr. James Miller', 'Bordetella', '2023-03-05', '2023-09-05', NOW());

-- Vaccinations for Bella (Dog - Labrador)
INSERT INTO vaccinations (pet_id, veterinarian_id, veterinarian_name, vaccine_name, date_given, next_due, created_at) VALUES
(2, 6, 'Dr. Sarah Johnson', 'Rabies', '2023-01-20', '2024-01-20', NOW()),
(2, 6, 'Dr. Sarah Johnson', 'DHPP', '2023-01-20', '2024-01-20', NOW()),
(2, 6, 'Dr. Sarah Johnson', 'Leptospirosis', '2023-01-20', '2024-01-20', NOW());

-- Vaccinations for Luna (Cat - Maine Coon)
INSERT INTO vaccinations (pet_id, veterinarian_id, veterinarian_name, vaccine_name, date_given, next_due, created_at) VALUES
(4, 1, 'Dr. Sarah Williams', 'Rabies', '2023-02-15', '2024-02-15', NOW()),
(4, 1, 'Dr. Sarah Williams', 'FVRCP', '2023-02-15', '2024-02-15', NOW()),
(4, 4, 'Dr. James Miller', 'FeLV', '2023-03-10', '2024-03-10', NOW());

-- Vaccinations for Buddy (Dog - Beagle)
INSERT INTO vaccinations (pet_id, veterinarian_id, veterinarian_name, vaccine_name, date_given, next_due, created_at) VALUES
(8, 6, 'Dr. Sarah Johnson', 'Rabies', '2023-03-01', '2024-03-01', NOW()),
(8, 6, 'Dr. Sarah Johnson', 'DHPP', '2023-03-01', '2024-03-01', NOW());