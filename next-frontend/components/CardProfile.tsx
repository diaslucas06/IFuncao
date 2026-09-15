interface CardProps {
    children: React.ReactNode,
    className?: string
}

export function CardBackground({ children, className }: CardProps) {
    return (
        <div className={`flex flex-col bg-(--profile-card-color) font-poppins-sans rounded-3xl shadow-xl p-5 md:px-5 md:py-6 lg:px-10 lg:py-8  ${className ? className: 'gap-[20px]'}`}>
            {children}
        </div>
    )
}

export function CardH1({ children }: CardProps) {
    return (
        <h1 className="font-extrabold text-xl md:text-[28px] lg:text-[32px] pc:text-[40px]">
            {children}
        </h1>
    )
}

export function CardLi({ children }: CardProps) {
    return (
        <li className="font-normal text-base md:text-xl lp:text-2xl pc:text-[32px]">
            {children}
        </li>
    )
}

export function CardP({ children }: CardProps) {
    return (
        <p className="font-medium md:text-xl lp:text-2xl">
            {children}
        </p>
    )
}

