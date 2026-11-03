# Database Design Exercise 5 Answers

姓名：易治行  
学号：2023141220023

## I. Automobile company database

### 1. ER design

Core entities are `Brand`, `Model`, `Option`, `Vehicle`, `Dealer`, `Customer`, and `VehicleOrder`.

- One brand offers many models; each model belongs to exactly one brand.
- `ModelOption` records the many-to-many set of options available for each model.
- Each vehicle is identified by a unique VIN and is an instance of exactly one model.
- `VehicleOption` records the options actually installed on a vehicle.
- A dealer holds many vehicles in inventory. A vehicle is assigned to one dealer in this system.
- A dealer places many vehicle orders. An order is for one model and may be associated with a customer; a null customer indicates an inventory order.
- `OrderOption` records the requested options for an order.
- An order may later be fulfilled by one vehicle; a vehicle can fulfill at most one order.
- When an order is fulfilled, it records the delivered VIN, delivery date, and sale price. This also preserves the customer's purchase history.

### 2. Relation schemas

```text
BRAND(brand_id, brand_name)
  PK: brand_id
  UNIQUE: brand_name

MODEL(model_id, brand_id, model_name)
  PK: model_id
  FK: brand_id -> BRAND(brand_id)
  UNIQUE: (brand_id, model_name)

OPTION(option_id, option_name, description)
  PK: option_id
  UNIQUE: option_name

MODEL_OPTION(model_id, option_id, option_price)
  PK: (model_id, option_id)
  FK: model_id -> MODEL(model_id)
  FK: option_id -> OPTION(option_id)

DEALER(dealer_id, dealer_name, address, phone)
  PK: dealer_id

CUSTOMER(customer_id, customer_name, phone, email, address)
  PK: customer_id

VEHICLE(VIN, model_id, dealer_id, inventory_status)
  PK: VIN
  FK: model_id -> MODEL(model_id)
  FK: dealer_id -> DEALER(dealer_id)

VEHICLE_OPTION(VIN, option_id)
  PK: (VIN, option_id)
  FK: VIN -> VEHICLE(VIN)
  FK: option_id -> OPTION(option_id)

VEHICLE_ORDER(order_id, dealer_id, customer_id, model_id,
              order_date, order_status, VIN, delivery_date, sale_price)
  PK: order_id
  FK: dealer_id -> DEALER(dealer_id)
  FK: customer_id -> CUSTOMER(customer_id), nullable
  FK: model_id -> MODEL(model_id)
  FK: VIN -> VEHICLE(VIN), nullable and UNIQUE

ORDER_OPTION(order_id, option_id)
  PK: (order_id, option_id)
  FK: order_id -> VEHICLE_ORDER(order_id)
  FK: option_id -> OPTION(option_id)
```

### 3. Additional constraints

1. `VIN`, all identifiers, names used as unique values, and required dates are not null.
2. `option_price >= 0` and `sale_price >= 0`.
3. `inventory_status` is restricted to values such as `ORDERED`, `IN_STOCK`, `RESERVED`, and `SOLD`.
4. `order_status` is restricted to values such as `PLACED`, `CONFIRMED`, `BUILT`, `DELIVERED`, and `CANCELLED`.
5. For every `VEHICLE_OPTION(VIN, option_id)`, the option must occur in `MODEL_OPTION` for that vehicle's model.
6. For every `ORDER_OPTION(order_id, option_id)`, the option must occur in `MODEL_OPTION` for the model named by the order.
7. If an order has a fulfillment VIN, the vehicle and the order must refer to the same model and dealer.
8. A delivered customer order must have non-null `VIN`, `delivery_date`, and `sale_price`; its vehicle must have `inventory_status = 'SOLD'`.
9. `delivery_date >= order_date` whenever a delivery date is present.

## II. Hospital database

### 1. ER design

Core entities are `Department`, `Employee`, `Doctor`, `Nurse`, `Patient`, and the associative entity `Hospitalization`.

- A department employs many employees; every employee works in exactly one department.
- `Doctor` and `Nurse` are disjoint, total subtypes of `Employee`.
- A patient can have many hospitalization records, and a department can receive many hospitalizations.
- `Hospitalization` resolves the many-to-many relationship between patients and departments. Its admission date distinguishes repeated stays by the same patient in the same department.

### 2. Relation schemas

```text
DEPARTMENT(department_no, department_name)
  PK: department_no
  UNIQUE: department_name

EMPLOYEE(employee_no, employee_name, gender, department_no, employee_type)
  PK: employee_no
  FK: department_no -> DEPARTMENT(department_no)

DOCTOR(employee_no, professional_title)
  PK: employee_no
  FK: employee_no -> EMPLOYEE(employee_no)

NURSE(employee_no)
  PK: employee_no
  FK: employee_no -> EMPLOYEE(employee_no)

PATIENT(patient_id, patient_name, gender, birth_date)
  PK: patient_id

HOSPITALIZATION(patient_id, department_no, admission_date, discharge_date)
  PK: (patient_id, department_no, admission_date)
  FK: patient_id -> PATIENT(patient_id)
  FK: department_no -> DEPARTMENT(department_no)
```

### 3. Additional constraints

1. Every employee has exactly one department, enforced by a non-null `department_no` foreign key.
2. `employee_type` is restricted to `DOCTOR` or `NURSE`.
3. The specialization is total and disjoint: each employee appears in exactly one of `DOCTOR` and `NURSE`, consistent with `employee_type`.
4. `gender` is restricted to the hospital's accepted domain values.
5. `discharge_date` may be null for a current stay; otherwise `discharge_date >= admission_date`.
6. Two hospitalization periods for the same patient must not overlap.
7. The composite primary key permits a patient to be admitted to the same department repeatedly, provided the admission dates differ.

