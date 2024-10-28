const { Button, ButtonToolbar, Modal, Schema, Form } = rsuite;
const { StringType } = Schema.Types;
const model = Schema.Model({
    dataActionId: StringType().isRequired("This field is required."),
    email: StringType()
        .isEmail("Please enter a valid email address.")
        .isRequired("This field is required.")
});

const Field = React.forwardRef((props, ref) => {
    const { name, message, label, accepter, error, ...rest } = props;
    return (
        <Form.Group
            controlId={`${name}-10`}
            ref={ref}
            className={error ? "has-error" : ""}
        >
            <Form.ControlLabel>{label} </Form.ControlLabel>
            <Form.Control
                name={name}
                accepter={accepter}
                errorMessage={error}
                {...rest}
            />
            <Form.HelpText>{message}</Form.HelpText>
        </Form.Group>
    );
});

const dataList = [
    { value: "chocolate", label: "Chocolate" },
    { value: "strawberry", label: "Strawberry" },
    { value: "vanilla", label: "Vanilla" }
];

const CustomSelect = React.forwardRef((props, ref) => {
    const { value, onChange, options, ...rest } = props;
    return (
        <select
            onChange={(option) => {
                onChange(option?.value || null);
            }}
            ref={ref}
            {...rest}
        >
            <option>Please choose one option</option>
            {options.map((option, index) => {
                return <option key={index}>{option.label}</option>;
            })}
        </select>
    );
});

function App() {
    const [open, setOpen] = React.useState(false);
    const handleOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);
    const formRef = React.useRef();
    const [formError, setFormError] = React.useState({});

    return (
        <>
            <ButtonToolbar>
                <Button onClick={handleOpen}> Open</Button>
            </ButtonToolbar>

            <Modal open={open} onClose={handleClose}>
                <h4>Titulo</h4>
                <Modal.Header>
                    <Modal.Title>Modal Title</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <Form model={model} ref={formRef}>
                        <Field
                            name="dataActionId"
                            label="Tipo de Movimiento"
                            accepter={CustomSelect}
                            options={dataList}
                            error={formError.foods}
                        />

                        <ButtonToolbar>
                            <Button appearance="primary" type="submit">
                                Submit
                            </Button>
                        </ButtonToolbar>
                    </Form>
                </Modal.Body>
                <Modal.Footer>
                    <Button onClick={handleClose} appearance="primary" type="submit">
                        Ok
                    </Button>
                    <Button onClick={handleClose} appearance="subtle">
                        Cancel
                    </Button>
                </Modal.Footer>
            </Modal>
        </>
    );
}
const html_root = document.getElementById('application');
const r = ReactDOM.createRoot(html_root).render(<App/>);


 
//ReactDOM.render(<App />, document.getElementById("application"));