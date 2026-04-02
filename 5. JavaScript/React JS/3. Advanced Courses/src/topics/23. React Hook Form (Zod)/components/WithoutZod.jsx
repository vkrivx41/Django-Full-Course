import React from 'react'
import { useForm } from 'react-hook-form'


const WithoutZod = () => {
    const { register, handleSubmit, setError, formState: { errors, isSubmitting } } = useForm()

    const submitForm = async (data) => {
        try {
            await new Promise(resolve => setTimeout(resolve, 1000))
            console.log(data)
            if (Math.random() > 0.5) throw new Error();
        } catch (error) {
            setError("root", {
                message: "Some errors occurred while submitting"
            })
        }
    }

    return (
        <form onSubmit={handleSubmit(submitForm)}>
            <h1>Hook Form Without Zod</h1>
            {errors.root && <div style={{ color: "darkred" }}>{errors.root.message}</div>}
            <div className="form-element">
                <label htmlFor="name">Name: </label>
                <input
                    type="text"
                    id='name'
                    placeholder='Name'
                    {...register("name", {
                        required: "Name is required",
                        minLength: {
                            value: 2,
                            message: "Name must be at least 2 characters"
                        }
                    })}
                />
                {errors.name && <div style={{ color: "darkred" }}>{errors.name.message}</div>}
            </div>
            <div className="form-element">
                <label htmlFor="email">Email: </label>
                <input
                    type="email"
                    id='email'
                    placeholder='Email'
                    {...register("email", {
                        required: "Email is required",
                        pattern: {
                            value: /^[a-z0-9-_.]+@[a-zA-Z0-9-.]+\.[a-zA-Z]+$/,
                            message: "Enter a valid email address"
                        }
                    })}
                />
                {errors.email && <div style={{ color: "darkred" }}>{errors.email.message}</div>}
            </div>
            <div className="form-element">
                <label htmlFor="age">Age: </label>
                <input
                    type="number"
                    id='age'
                    placeholder='Age'
                    {...register("age", {
                        required: "Age is required",
                        valueAsNumber: true,
                        min: {
                            value: 18,
                            message: "Age must be greater than or equal to 18"
                        },
                        max: {
                            value: 99,
                            message: "Age must be less than or equal to 99"
                        }
                    })}
                />
                {errors.age && <div style={{ color: "darkred" }}>{errors.age.message}</div>}
            </div>
            <div className="form-element">
                <label htmlFor="gender">Gender: </label>
                <select
                    id="gender"
                    {...register("gender", {
                        required: "Gender is required",
                        validate: (value) => {
                            if (!['male', 'female', 'none'].includes(value)) {
                                return "Gender must be valid"
                            }
                        }
                    })}
                >
                    <option value="male">Male</option>
                    <option value="female">Female</option>
                    <option value="none">Rather Not Say</option>
                </select>
                {errors.gender && <div style={{ color: "darkred" }}>{errors.gender.message}</div>}
            </div>
            <div className="form-element">
                <label htmlFor="address">Address: </label>
                <input
                    type="text"
                    id='address'
                    placeholder='City'
                    {...register("address.city", {
                        required: "City is required",
                        min: {
                            value: 2,
                            message: "City name must be at least 2 characters"
                        }
                    })}
                />
                {errors.address?.city && <div style={{ color: "darkred" }}>{errors.address?.city.message}</div>}
                <input
                    type="text"
                    placeholder='Street'
                    {...register("address.street", {
                        required: true,
                        min: 2
                    })}
                />
                {errors.address?.street && <div style={{ color: "darkred" }}>{errors.address?.street.message}</div>}
            </div>
            <div className="form-element">
                <label htmlFor="password">Password: </label>
                <input
                    type="password"
                    id='password'
                    placeholder='Password'
                    {...register("password", {
                        required: "Password is required",
                        min: {
                            value: 6,
                            message: "Password must be at least 6 characters"
                        },
                        max: {
                            value: 30,
                            message: "Password must be at most 30 characters"
                        }
                    })}
                />
                {errors.password && <div style={{ color: "darkred" }}>{errors.password.message}</div>}
            </div>
            <div className="form-element">
                <button
                    type='submit'
                    disabled={isSubmitting}
                >{isSubmitting ? "Loading..." : "Submit"}</button>
            </div>
        </form>
    )
}

export default WithoutZod
