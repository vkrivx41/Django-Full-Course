import React from 'react'
import { useFieldArray, useForm } from 'react-hook-form'
import { z } from 'zod'
import { zodResolver } from '@hookform/resolvers/zod'
import { fields } from '@hookform/resolvers/ajv/src/__tests__/__fixtures__/data.js'


const schema = z.object({
    name: z.string().min(2, "Name must be at least 2 characters"),
    email: z.email("Enter a valid email address"),
    age: z.number("Age is required")
        .min(18, "Age must be greater than or equal to 18")
        .max(99, "Age must be less than or equal to 99"),
    gender: z.enum(['male', 'female', 'none'], "Gender must be valid"),
    address: z.object({
        city: z.string().min(2, "City name must be at least 2 characters"),
        street: z.string().min(2, "Street name must be at least 2 characters"),
    }),
    hobbies: z.array(
        z.object({
            name: z.string().min(1, "Hobby name is required")
        })
    ).min(1, "At least one hobby is required"),
    password: z.string()
        .min(6, "Password must be at least 6 characters")
        .max(30, "Password must be at most 30 characters")
})


const WithZod = () => {
    const { register, handleSubmit, control, setError, formState: { errors, isSubmitting } } = useForm({
        resolver: zodResolver(schema)
    })

    const { fields, append, remove } = useFieldArray({
        control,
        name: "hobbies"
    })

    const submitForm = async (data) => {
        try {
            await new Promise(resolve => setTimeout(resolve, 1))
            console.log(data)
            // if (Math.random() > 0.5) throw new Error();
        } catch (error) {
            setError("root", {
                message: "Some errors occurred while submitting"
            })
        }
    }

    return (
        <form onSubmit={handleSubmit(submitForm)}>
            <h1>Hook Form With Zod</h1>
            {errors.root && <div style={{ color: "darkred" }}>{errors.root.message}</div>}
            <div className="form-element">
                <label htmlFor="name">Name: </label>
                <input
                    type="text"
                    id='name'
                    placeholder='Name'
                    {...register("name")}
                />
                {errors.name && <div style={{ color: "darkred" }}>{errors.name.message}</div>}
            </div>
            <div className="form-element">
                <label htmlFor="email">Email: </label>
                <input
                    type="email"
                    id='email'
                    placeholder='Email'
                    {...register("email")}
                />
                {errors.email && <div style={{ color: "darkred" }}>{errors.email.message}</div>}
            </div>
            <div className="form-element">
                <label htmlFor="age">Age: </label>
                <input
                    type="number"
                    id='age'
                    placeholder='Age'
                    {...register("age", { valueAsNumber: true })}
                />
                {errors.age && <div style={{ color: "darkred" }}>{errors.age.message}</div>}
            </div>
            <div className="form-element">
                <label htmlFor="gender">Gender: </label>
                <select
                    id="gender"
                    {...register("gender")}
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
                    {...register("address.city")}
                />
                {errors.address?.city && <div style={{ color: "darkred" }}>{errors.address.city.message}</div>}
                <input
                    type="text"
                    placeholder='Street'
                    {...register("address.street")}
                />
                {errors.address?.street && <div style={{ color: "darkred" }}>{errors.address.street.message}</div>}
            </div>
            <div className="form-element">
                <label htmlFor="hobbies">Hobbies: </label>
                {fields.map((hobby, index) => (
                    <div key={index}>
                        <input
                            type="text"
                            placeholder='Hobby'
                            {...register(`hobbies.${index}.name`)}
                        />
                        <button type='button' onClick={() => remove({ name: hobby })}>Remove Hobby</button>
                        {errors.hobbies?.[index]?.name && <div style={{ color: "darkred" }}>{errors.hobbies[index].name.message}</div>}
                    </div>
                ))}
                <button type='button' onClick={() => append({ name: "" })}>Add Hobby</button>
                {errors.hobbies?.root && <div style={{ color: "darkred" }}>{errors.hobbies.root.message}</div>}
            </div>
            <div className="form-element">
                <label htmlFor="password">Password: </label>
                <input
                    type="password"
                    id='password'
                    placeholder='Password'
                    {...register("password")}
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

export default WithZod
